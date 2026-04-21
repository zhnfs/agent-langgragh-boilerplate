import os
from mcp.server.fastmcp import FastMCP
from tavily import TavilyClient

from dotenv import load_dotenv
load_dotenv()

# Load Tavily API key from environment
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
client = TavilyClient(api_key=TAVILY_API_KEY)

mcp = FastMCP("Tavily MCP Server")

@mcp.tool()
def search(query: str) -> str:
    """Handle search requests via Tavily."""
    result = client.search(query)
    return result

if __name__ == "__main__":
    mcp.run()
