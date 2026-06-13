import json
import os
from typing import List, Dict, Any
from client import OllamaClient
from tools import get_tool_schemas, execute_tool

def load_config() -> Dict[str, Any]:
    with open("config.json", "r") as f:
        return json.load(f)

def save_log(messages: List[Dict[str, Any]]):
    os.makedirs("logs", exist_ok=True)
    with open("logs/session_latest.json", "w") as f:
        json.dump(messages, f, indent=2)

def main():
    config = load_config()
    client = OllamaClient(
        api_url=config["api_url"],
        model=config["model"],
        timeout=config.get("timeout")
    )
    
    tools = get_tool_schemas()
    
    messages = [
        {
            "role": "system",
            "content": config["system_prompt"]
        }
    ]
    
    print("Welcome to GravityCore.")
    print(f"Model: {config['model']}")
    print("Type your request. Type 'exit' to quit.")
    
    while True:
        try:
            user_input = input("\n[User]> ")
        except (KeyboardInterrupt, EOFError):
            break
            
        if user_input.strip().lower() in ['exit', 'quit']:
            break
            
        if not user_input.strip():
            continue
            
        messages.append({"role": "user", "content": user_input})
        
        # Enter the ReAct loop
        while True:
            save_log(messages)
            print("[GravityCore] Thinking...")
            
            try:
                response = client.chat(messages, tools)
            except Exception as e:
                print(f"[Error] {e}")
                break
                
            message = response.get("message", {})
            messages.append(message)
            
            if "tool_calls" in message and message["tool_calls"]:
                # Print the content if any before the tool call
                if message.get("content"):
                    print(f"[Agent] {message['content']}")
                    
                # Execute tools
                for tool_call in message["tool_calls"]:
                    func_name = tool_call["function"]["name"]
                    args = tool_call["function"]["arguments"]
                    print(f"  [Tool Call] -> {func_name}({json.dumps(args)})")
                    
                    # Execute
                    result = execute_tool(func_name, args)
                    
                    # Add tool response to messages
                    messages.append({
                        "role": "tool",
                        "content": str(result),
                        "name": func_name
                    })
            else:
                # No more tool calls, print final response
                if message.get("content"):
                    print(f"[Agent] {message['content']}")
                break
                
    print("Exiting GravityCore.")

if __name__ == "__main__":
    main()
