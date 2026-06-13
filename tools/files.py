import os

def read_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

def write_file(path: str, content: str, mode: str = "w") -> str:
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with open(path, mode, encoding="utf-8") as f:
            f.write(content)
        return f"Successfully wrote to {path}"
    except Exception as e:
        return f"Error writing file: {str(e)}"

read_file_tool = {
    "func": read_file,
    "schema": {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Reads the contents of a local file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "The absolute or relative path to the file."
                    }
                },
                "required": ["path"]
            }
        }
    }
}

write_file_tool = {
    "func": write_file,
    "schema": {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Writes or appends content to a local file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "The path to the file."
                    },
                    "content": {
                        "type": "string",
                        "description": "The content to write to the file."
                    },
                    "mode": {
                        "type": "string",
                        "enum": ["w", "a"],
                        "description": "File mode: 'w' for overwrite, 'a' for append. Defaults to 'w'."
                    }
                },
                "required": ["path", "content"]
            }
        }
    }
}
