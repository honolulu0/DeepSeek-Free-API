import requests
import json
from datetime import datetime

# Configuration
BASE_URL = "http://localhost:8000"
API_ENDPOINT = "/v1/chat/completions"
TOKEN = "3CQdrZNAIXDE6lG9PSEBkXRgQir3S5Mc7P5+BWG/8H3+SPDMX8BIHU/umXztvQQf"

def test_stream_debug():
    """测试流式模式，记录完整原始数据到日志文件"""
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
        "stream": True,
        "thinking_enabled": True,
        "search_enabled": True
    }
    
    log_file = f"stream_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    print(f"Testing stream mode with thinking and search enabled...")
    print(f"Logging to: {log_file}")
    print("-" * 50)
    
    try:
        response = requests.post(url, headers=headers, json=payload, stream=True, timeout=120)
        
        print(f"Status Code: {response.status_code}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        print("-" * 50)
        
        if response.status_code == 200:
            with open(log_file, 'w', encoding='utf-8') as f:
                f.write(f"Request: {json.dumps(payload, ensure_ascii=False, indent=2)}\n")
                f.write(f"Status: {response.status_code}\n")
                f.write("-" * 50 + "\n\n")
                
                for i, line in enumerate(response.iter_lines()):
                    if line:
                        decoded = line.decode('utf-8')
                        f.write(f"[{i}] {decoded}\n")
                        
                        # 解析并格式化输出
                        if decoded.startswith('data: ') and decoded != 'data: [DONE]':
                            try:
                                data = json.loads(decoded[6:])
                                f.write(f"    -> Parsed: {json.dumps(data, ensure_ascii=False)}\n")
                            except:
                                pass
                        
                        print(f"[{i}] {decoded[:100]}{'...' if len(decoded) > 100 else ''}")
                        
                        if '[DONE]' in decoded:
                            break
            
            print(f"\nFull log saved to: {log_file}")
        else:
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_stream_debug()
