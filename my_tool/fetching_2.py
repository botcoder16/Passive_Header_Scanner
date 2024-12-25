import requests

def fetch_response_headers(url):
    try:
        # Sending a GET request to the specified URL
        response = requests.get(url[0])
        
        # Fetching the status code
        status_code = response.status_code
        
        # Fetching response headers
        headers = response.headers
        
        # Displaying the fetched details
        print(f"Status Code: {status_code}")
        print("Response Headers:")
        for key, value in headers.items():
            print(f"{key}:---> {value}")
            print('------------------------------------------')
        
        # Return the response headers for further processing
        return headers
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []