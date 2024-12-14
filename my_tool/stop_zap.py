import requests

# Define ZAP API URL and API key
zap_url = 'http://localhost:8081/'  # Adjust this if your ZAP is running on a different host or port
api_key = 'tbbt3k58avsru4cf389ct2p6f3'  # Replace with your actual API key

# Function to shutdown ZAP
def shutdown_zap():
    try:
        # Send shutdown request to ZAP API with API key
        response = requests.get(zap_url + 'JSON/core/action/shutdown/', params={'apikey': api_key})
        
        # Check if the shutdown request was successful
        if response.status_code == 200:
            print("ZAP has been requested to shut down.")
        else:
            print("Failed to send shutdown request. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error communicating with ZAP API:", e)

# Call the function to shutdown ZAP
shutdown_zap()
