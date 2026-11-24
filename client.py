# import asyncio
# from mcp import ClientSession
# from mcp.client.streamable_http import streamable_http_client

# URL = "https://siliconbricks.co/hiring/mcp"


# async def main():
#     async with streamable_http_client(URL) as (read, write):
#         async with ClientSession(read, write) as session:
#             info = await session.initialize()
#             print("SERVER:", info.server_info)
#             # print("SERVER:", info.serverInfo)
#             print("INSTRUCTIONS:", info.instructions)

#             tools = await session.list_tools()
#             for t in tools.tools:
#                 print("\nTOOL:", t.name, "-", t.description)
#                 print("  input:", t.input_schema)

#             for name, fn in [("RESOURCE", session.list_resources), ("PROMPT", session.list_prompts)]:
#                 try:
#                     res = await fn()
#                     items = getattr(res, "resources", None) or getattr(res, "prompts", [])
#                     for i in items:
#                         print(f"\n{name}:", getattr(i, "uri", None) or i.name, "-", i.description)
#                 except Exception as e:
#                     print(f"\n{name}S not supported:", e)
#             result = await session.call_tool("get_assignment", {})
#             for c in result.content:
#                 print(c.text)

# asyncio.run(main())



import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

URL = "https://siliconbricks.co/hiring/mcp"
lines = []


def out(*args):
    text = " ".join(str(a) for a in args)
    print(text)
    lines.append(text)


async def main():
    async with streamable_http_client(URL) as (read, write):
        async with ClientSession(read, write) as session:
            info = await session.initialize()
            out("SERVER:", info.server_info)
            out("INSTRUCTIONS:", info.instructions)

            tools = await session.list_tools()
            for t in tools.tools:
                out("\nTOOL:", t.name, "-", t.description)
                out("  input:", t.input_schema)

            for name, fn in [("RESOURCE", session.list_resources), ("PROMPT", session.list_prompts)]:
                try:
                    res = await fn()
                    items = getattr(res, "resources", None) or getattr(res, "prompts", [])
                    for i in items:
                        out(f"\n{name}:", getattr(i, "uri", None) or i.name, "-", i.description)
                except Exception as e:
                    out(f"\n{name}S not supported:", e)

            result = await session.call_tool("get_assignment", {})
            for c in result.content:
                out(c.text)

    with open("assignment.md", "w") as f:
        f.write("\n".join(lines))


asyncio.run(main())