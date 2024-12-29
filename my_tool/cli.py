from core import normal_scan
import argparse
import re

def main():
    parser = argparse.ArgumentParser(description="Welcome to the Passive scanner")
    parser.add_argument("action", help="The action to perform", choices=["run", "status"])
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    # Step 1: Define the options to display
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
    print()    
    normal_scan(urls)
    
main()
