import requests
import json
import sys

# Configuration
BASE_URL = "http://101.201.214.215:8000"
API_ENDPOINT = "/token/check"

# Default token to test (can be overridden by command line argument)
DEFAULT_TOKEN = "3CQdrZNAIXDE6lG9PSEBkXRgQir3S5Mc7P5+BWG/8H3+SPDMX8BIHU/umXztvQQf"

def test_token_check(token=None):
    if token is None:
        token = DEFAULT_TOKEN
        
    url = f"{BASE_URL}{API_ENDPOINT}"
    
    payload = {
        "token": token
    }
    
    print(f"Testing token: {token[:10]}...")
    print(f"Sending request to {url}...")
    
    try:
        response = requests.post(url, json=payload)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                print("Response JSON:")
                print(json.dumps(data, indent=2))
                
                if data.get('live') is True:
                    print("✅ Token is valid (live)")
                else:
                    print("❌ Token is invalid (not live)")
                    
            except json.JSONDecodeError:
                print("Error decoding JSON response")
                print(response.text)
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print(f"❌ Could not connect to {BASE_URL}. Is the server running?")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Allow passing token as command line argument
    token_arg = None
    if len(sys.argv) > 1:
        token_arg = sys.argv[1]
    
    test_token_check(token_arg)
