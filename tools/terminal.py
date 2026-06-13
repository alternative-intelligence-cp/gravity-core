import subprocess

def run_command(command: str) -> str:
    try:
        # Use a timeout to prevent runaway processes
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=120
        )
        output = result.stdout
        if result.stderr:
            output += f"\nSTDERR:\n{result.stderr}"
        return output.strip() if output.strip() else "Command executed successfully with no output."
    except subprocess.TimeoutExpired:
        return "Error: Command timed out after 120 seconds."
    except Exception as e:
        return f"Error: {str(e)}"

run_command_tool = {
    "func": run_command,
    "schema": {
        "type": "function",
        "function": {
            "name": "run_command",
            "description": "Executes a shell command on the local terminal and returns its output.",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The bash command to execute."
                    }
                },
                "required": ["command"]
            }
        }
    }
}
