from datetime import datetime


def after_tool_callback(tool, args, tool_context, tool_response):
    print("\n==============================")
    print("✅ AFTER TOOL CALLBACK")
    print(f"Time : {datetime.now()}")
    print(f"Tool : {tool.name}")
    print(f"Result : {tool_response}")
    print("==============================")

    return None