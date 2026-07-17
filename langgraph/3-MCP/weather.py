from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")


@mcp.tool()
async def get_weather(location: str) -> str:
    """Get the weather location
    """
    return f"It's always raining in {location}"


# * transport="streamable-http" --> runs as an http server http://127.0.0.1:8000
# For example:
# (tutorial) root@df0261ca4c50:/app# python langgraph/3-MCP/weather.py 
# INFO:     Started server process [11446]
# INFO:     Waiting for application startup.
# [07/17/26 14:20:52] INFO     StreamableHTTP session manager started                                                                                                                                                                                                         streamable_http_manager.py:131
# INFO:     Application startup complete.
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")