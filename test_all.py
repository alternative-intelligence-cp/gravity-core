import json
from client import OllamaClient
from tools.terminal import run_command
from tools.files import read_file, write_file

def test():
    print("1. Testing Files...")
    write_file("test_artifact.txt", "Hello World!")
    content = read_file("test_artifact.txt")
    print(f"File content: {content}")

    print("\n2. Testing Terminal...")
    out = run_command("whoami")
    print(f"whoami: {out}")
    
    print("\n3. Testing Client (Simple Ping)...")
    try:
        client = OllamaClient("http://localhost:11434/api/chat", "devstral-2:123b:cloud", timeout=120)
        # Just send a simple hello
        res = client.chat([{"role": "user", "content": "Say 'Test Successful!'"}])
        print(f"Client response: {res.get('message', {}).get('content')}")
    except Exception as e:
        print(f"Client failed: {e}")

if __name__ == '__main__':
    test()
