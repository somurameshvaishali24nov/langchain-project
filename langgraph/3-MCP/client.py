from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio
import os

MATH_SERVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mathserver.py")


async def main():
    client = MultiServerMCPClient(
        {
            "math": { # tool 1
                "command": "python",
                "args": [MATH_SERVER_PATH], ### Esnure correct absolutepath
                "transport": "stdio"
            },
            "weather": { # tool 2
                "url": "http://127.0.0.1:8000/mcp", ## Ensure that server is running here
                "transport": "streamable-http"
            },
        }
    )

    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model = ChatGroq(model="qwen/qwen3-32b")
    agent = create_agent(
        model=model, 
        tools=tools
    )
    
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is (3 + 5) x 12 ?"}]}
    )
    print("Math response", math_response["messages"][-1].content)

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is the weather in California?"}]}
    )
    print("Weather response", weather_response["messages"][-1].content)


asyncio.run(main=main())