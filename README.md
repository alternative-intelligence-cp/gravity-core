# GravityCore

GravityCore is a highly capable autonomous AI assistant framework designed to interact seamlessly with local and remote systems. Powered by Ollama, it implements a robust ReAct (Reasoning and Acting) loop to autonomously plan and execute tools to fulfill user requests.

## Features

- **ReAct Agent Loop**: Utilizes a dynamic loop allowing the AI to reason about tasks and execute tools in sequence to achieve complex goals.
- **Ollama Integration**: Natively interfaces with Ollama API for high-performance inference, configurable with various models.
- **Robust Client**: Built-in exponential backoff and error handling for reliable API communication.
- **Tool System**: Easily extensible tool schema allowing the agent to access the filesystem, run terminal commands, and perform other tasks autonomously.
- **Session Logging**: Automatically saves session logs for analysis, debugging, and continuous improvement.

## Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com/) running locally or accessible via network.
- Recommended: A robust model such as `devstral-2:123b:cloud` or equivalent.

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:alternative-intelligence-cp/gravity-core.git
   cd gravity-core
   ```

2. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Edit `config.json` to configure the assistant:

```json
{
  "api_url": "http://localhost:11434/api/chat",
  "model": "devstral-2:123b:cloud",
  "timeout": null,
  "system_prompt": "You are a highly capable AI assistant operating via GravityCore. You have access to a set of tools to interact with the system. Work autonomously to fulfill the user's requests."
}
```

- `api_url`: The endpoint for your Ollama instance.
- `model`: The specific model to use for inference.
- `timeout`: Request timeout in seconds (null for no timeout).
- `system_prompt`: The core instruction set guiding the agent's behavior.

## Usage

Start the GravityCore assistant by running the main entry point:

```bash
python core.py
```

You will be greeted by the interactive prompt:
```
Welcome to GravityCore.
Model: devstral-2:123b:cloud
Type your request. Type 'exit' to quit.

[User]> 
```

Enter your request and the agent will begin reasoning and executing tools. Type `exit` or `quit` to end the session.

## Testing

To run the test suite:
```bash
python test_all.py
```

## Logs

All sessions are logged automatically to the `logs/` directory. The most recent session is saved as `logs/session_latest.json`.

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for full details.
