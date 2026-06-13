from typing import Dict, Any, Callable
from .terminal import run_command_tool
from .files import read_file_tool, write_file_tool

# Registry of all available tools
TOOLS_REGISTRY: Dict[str, Dict[str, Any]] = {}

def register_tool(func: Callable, schema: Dict[str, Any]):
    TOOLS_REGISTRY[schema['function']['name']] = {
        "func": func,
        "schema": schema
    }

# Register tools
register_tool(run_command_tool['func'], run_command_tool['schema'])
register_tool(read_file_tool['func'], read_file_tool['schema'])
register_tool(write_file_tool['func'], write_file_tool['schema'])

def get_tool_schemas() -> list:
    return [t["schema"] for t in TOOLS_REGISTRY.values()]

def execute_tool(name: str, arguments: Dict[str, Any]) -> str:
    if name not in TOOLS_REGISTRY:
        return f"Error: Tool '{name}' not found."
    
    try:
        return TOOLS_REGISTRY[name]["func"](**arguments)
    except Exception as e:
        return f"Error executing '{name}': {str(e)}"
