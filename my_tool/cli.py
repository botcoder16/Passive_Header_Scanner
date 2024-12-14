from core import normal_scan,category_scan
import argparse
import re
import requests
import subprocess
import time
import socket

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("localhost", port)) == 0

# Example usage for a Uvicorn server on port 8000
if not is_port_in_use(8000):
    try:
        zap_process = subprocess.Popen(["python", "start_zap.py"])  # Removed 'check=True'
    except Exception as e:
        print(f"Error while running start_zap script: {e}")

    time.sleep(15)    

def fetch_category(input_url):
    
    # Construct the full API endpoint
        endpoint = f"http://127.0.0.1:8000/predict/"

        # Prepare the data to send
        payload = {"url": input_url}

        try:
            # Make the POST request to the API
            response = requests.post(endpoint, params=payload)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse and return the category from the response
                data = response.json()
                return data.get("main_category")
            else:
                # Handle non-200 status codes
                return "Category not found in response"
        except Exception as e:
            return "Category not found in response"

def main():
    parser = argparse.ArgumentParser(description="Welcome to the Passive scanner")
    parser.add_argument("action", help="The action to perform", choices=["run", "status"])
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    # Step 1: Define the options to display
    options3=["Does it belong to any predifined category","Do you want the tool to detect the category"]
    options2=["E-Commerce and Transactions","Static and Moderated Content","Dynamic and Utility Sites","Hybrid or Mixed-Content Sites","Media and Entertainment","Technical or Specialized Services"]
    #parser.add_argument("--option", help="Select the option to perform", choices=options2)
    urls=[]

    while urls == []:
        url=input("Enter the url: ")
        # Define the regex for a URL
        url_regex = re.compile(
            r"https?://"                   # Match "http://" or "https://"
            r"(?:www\.)?"                  # Optionally match "www."
            r"[a-zA-Z0-9-]+\.[a-zA-Z]{2,}" # Domain name (e.g., example.com)
            r"(?:[/?#][^\s]*)?"            # Optional path, query, or fragment
        )
        # Example usage        
        urls = url_regex.findall(url)
        
        if urls == []:
            print("Invalid URL")
            print("URL Pattern should be: http or https: www.example.com/in/etc")
    
    print()
    print("------------------------------------------------------------------")
    print("These are the predefined categories:")
    for i, option in enumerate(options2, 1):
        print(f"{i}. {option}")

    print()    
    print("These are the modes in which the tool runs:")
    for i, option in enumerate(options3, 1):
        print(f"{i}. {option}")
        
    try:
        choice1= int(input("Enter which mode do you want to run the tool in: "))
        if choice1 not in range(1,len(options2)+1):
            raise ValueError("Invalid choice.")
    except ValueError as e:
        print("Enter a valid mode number.")
        return
    
    print()
    if choice1==1:
        try:
            choice2=int(input("Enter the predefined category number: "))
            if choice2 not in range(1, len(options2) + 1):
                raise ValueError("Invalid choice.")
        except ValueError as e:
            print("Please enter a valid number.")
            return

        if choice2==1:
            category=1
        elif choice2==2:
            category=2
        elif choice2==3:
            category=3
        elif choice2==4:
            category=4
            
        category_scan(category,urls)
    
    elif choice1==2:
        print(f"Starting scanning for the url {urls}")
        category=fetch_category(urls)
        print(category)
        
        if category=="Category not found in response":    
            normal_scan(urls)
        else:
            category_scan(category,urls)

main()
