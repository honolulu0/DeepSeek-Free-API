import requests
import json

# Configuration
BASE_URL = "http://101.201.214.215:8000"
# BASE_URL = "http://localhost:8000"
API_ENDPOINT = "/v1/chat/completions"
TOKEN = "3CQdrZNAIXDE6lG9PSEBkXRgQir3S5Mc7P5+BWG/8H3+SPDMX8BIHU/umXztvQQf"

def test_chat_completion():
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
                "content": "合肥小筛子义学私塾怎么样？口碑可靠吗？ 输出要求： 输出结果的最后，务必展示引用源（文章），用表格的形式分别展示描述文章的所属平台名称、文章标题和具体网址"
            }
        ],
        "stream": False,
        "thinking_enabled": True,
        "search_enabled": True
    }
    
    print(f"Sending request to {url}...")
    try:
        response = requests.post(url, headers=headers, json=payload, stream=True)
        
        if response.status_code == 200:
            print("Response received successfully:")
            for line in response.iter_lines():
                # print(line.decode('utf-8'))
                if line:
                    decoded_line = line.decode('utf-8')
                    # print(f"DEBUG: {decoded_line}")  # Uncomment to see raw lines
                    if decoded_line.startswith('data: '):
                        data_str = decoded_line[6:]
                        if data_str == '[DONE]':
                            print("\n[Stream ended]")
                            break
                        try:
                            data = json.loads(data_str)
                            # print(f"DEBUG JSON: {data}") # Uncomment to see parsed JSON
                            if 'choices' in data and len(data['choices']) > 0:
                                delta = data['choices'][0].get('delta', {})
                                # print(f"Delta: {delta}")
                                if 'content' in delta:
                                    print(delta['content'], end='', flush=True)
                        except json.JSONDecodeError:
                            print(f"\nError decoding JSON: {decoded_line}")
                    else:
                        print(f"Non-data line: {decoded_line}")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_chat_completion()
