from zapv2 import ZAPv2
import time

# Initialize the ZAP API client
zap = ZAPv2(apikey='fsem2celt7bged0jt6q8anhges', proxies={'http': 'http://127.0.0.1:8081', 'https': 'http://127.0.0.1:8081'})

# Target URL to spider and capture traffic
# Start spidering the target URL to generate traffic
    

def fetch_messages(url):
    target_url=url
    zap.pscan.set_enabled(False)
    print(f"Starting spider for target: {target_url}")
    spider_id = zap.spider.scan(target_url, maxchildren=10)
    
    # Wait for the spider to complete
    while int(zap.spider.status(spider_id)) < 100:
        print(f"Spider progress: {zap.spider.status(spider_id)}%")
        time.sleep(2)

    print("Spidering complete.")
    # Fetch all captured HTTP messages using the Core API's messages endpoint
    messages = zap.core.messages(baseurl=target_url,start=0,count=100)

    request_headers=()
    response_headers=()
    for message in messages:
        message_id = message['id']
        http_message = zap.core.message(message_id)
        
        
        # Initialize an empty dictionary to hold the key-value pairs
        requestHeader_dict = {}
        responseHeader_dict = {}

        # Split the header by new lines
        requestLines = http_message['requestHeader'].split("\n")
        responseLines = http_message['responseHeader'].split("\n")

        if requestLines:
            requestHeader_dict['url'] = requestLines[0].strip()
        
        if responseLines:
            responseHeader_dict['url']=responseLines[0].strip()
            if "HTTP/1.0 0" in responseHeader_dict["url"] or "404 Not Found" in responseHeader_dict["url"] or "403 Forbidden" in responseHeader_dict["url"]:
                continue
    
        # Loop through each line and split by ':'
        for line in requestLines:
            if ': ' in line:
                key, value = line.split(": ", 1)  # Split at the first colon only
                requestHeader_dict[key.strip()] = value.strip()
        
        for line in responseLines:
            if ': ' in line:
                key, value = line.split(": ",1)
                responseHeader_dict[key.strip()] = value.strip()
        
        request_headers += (requestHeader_dict,)
        response_headers += (responseHeader_dict,)
        # print("==== HTTP Message ====")
        # print("Request Header: ")
        # pprint.pprint(requestHeader_dict)
        # print("Response Header: ")
        # pprint.pprint(responseHeader_dict)
        
    return request_headers,response_headers

# if __name__ == "__main__":
#     # Start spidering to generate HTTP traffic

#     # Fetch the captured HTTP messages
#     http_messages = fetch_messages()
#     print(f"Number of HTTP messages captured: {len(messages)}")
