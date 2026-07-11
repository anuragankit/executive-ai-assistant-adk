from datetime import datetime


def before_tool_callback(tool, args, tool_context):
    print("\n==============================")
    print("🚀 BEFORE TOOL CALLBACK")
    print(f"Time : {datetime.now()}")
    print(f"Tool : {tool.name}")
    print(f"Args : {args}")
    print("==============================")

    return None