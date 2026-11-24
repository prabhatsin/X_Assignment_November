import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

URL = "https://siliconbricks.co/hiring/mcp"


async def main():
    async with streamable_http_client(URL) as (read, write, _):
        async with ClientSession(read, write) as session:
            info = await session.initialize()
            print("SERVER:", info.serverInfo)
            print("INSTRUCTIONS:", info.instructions)

            tools = await session.list_tools()
            for t in tools.tools:
                print("\nTOOL:", t.name, "-", t.description)
                print("  input:", t.inputSchema)

            for name, fn in [("RESOURCE", session.list_resources), ("PROMPT", session.list_prompts)]:
                try:
                    res = await fn()
                    items = getattr(res, "resources", None) or getattr(res, "prompts", [])
                    for i in items:
                        print(f"\n{name}:", getattr(i, "uri", None) or i.name, "-", i.description)
                except Exception as e:
                    print(f"\n{name}S not supported:", e)


asyncio.run(main())