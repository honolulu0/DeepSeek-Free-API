import requests
import json

# Configuration
BASE_URL = "http://localhost:8000"
API_ENDPOINT = "/v1/chat/completions"
TOKEN = "3CQdrZNAIXDE6lG9PSEBkXRgQir3S5Mc7P5+BWG/8H3+SPDMX8BIHU/umXztvQQf"

def test_non_stream():
    url = f"{BASE_URL}{API_ENDPOINT}"
    
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "user",
                "content": "北京今天天气怎么样"
            }
        ],
        "stream": False,
        "thinking_enabled": True,
        "search_enabled": True
    }
    
    print(f"Testing non-stream mode...")
    print(f"URL: {url}")
    print(f"Payload: {json.dumps(payload, ensure_ascii=False, indent=2)}")
    print("-" * 50)
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=120)
        
        print(f"Status Code: {response.status_code}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        print("-" * 50)
        
        if response.status_code == 200:
            try:
                data = response.json()
                print("Response JSON:")
                print(json.dumps(data, ensure_ascii=False, indent=2))
                
                # 提取关键信息
                if 'choices' in data and len(data['choices']) > 0:
                    message = data['choices'][0].get('message', {})
                    content = message.get('content', '')
                    reasoning = message.get('reasoning_content', '')
                    
                    print("-" * 50)
                    print("Content:")
                    print(content)
                    if reasoning:
                        print("\nReasoning Content:")
                        print(reasoning)
            except json.JSONDecodeError:
                print("Response is not JSON:")
                print(response.text[:1000])
        else:
            print(f"Error Response:")
            print(response.text)
            
    except requests.exceptions.Timeout:
        print("Request timed out (120s)")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_non_stream()
