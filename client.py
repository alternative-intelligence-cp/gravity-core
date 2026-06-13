import httpx
import json
import time
from typing import List, Dict, Any

class OllamaClient:
    def __init__(self, api_url: str, model: str, timeout: int | float | None = None):
        self.api_url = api_url
        self.model = model
        self.timeout = timeout
        
    def chat(self, messages: List[Dict[str, Any]], tools: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Sends a chat request to Ollama and handles exponential backoff.
        """
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False
        }
        
        if tools:
            payload["tools"] = tools

        max_retries = 5
        base_delay = 2

        for attempt in range(max_retries):
            try:
                # timeout=None disables the timeout completely in httpx
                with httpx.Client(timeout=self.timeout) as client:
                    response = client.post(self.api_url, json=payload)
                    response.raise_for_status()
                    return response.json()
            except httpx.RequestError as e:
                print(f"[Client Error] Network issue: {e}")
            except httpx.HTTPStatusError as e:
                print(f"[Client Error] HTTP Status {e.response.status_code}: {e.response.text}")
                # Don't retry on 400 Bad Request
                if e.response.status_code == 400:
                    raise
                
            if attempt < max_retries - 1:
                sleep_time = base_delay * (2 ** attempt)
                print(f"[Client] Retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)
                
        raise Exception("Failed to communicate with Ollama after multiple retries.")
