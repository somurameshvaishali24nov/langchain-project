# See the image of lang-ex13 and kang-ex14

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int):
    """Add 2 numbers
    """
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply 2 numbers
    """
    return a * b


# * The transport="stdio" argument tells the server to:
# Use Standard input/output (stdin and stdout) to receive and respond to tool function calls.
if __name__ == "__main__":
    mcp.run(transport="stdio") 