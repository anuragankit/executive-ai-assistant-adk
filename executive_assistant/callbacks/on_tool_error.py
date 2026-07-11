from datetime import datetime


def on_tool_error_callback(
    tool,
    args,
    tool_context,
    error,
):
    print("\n==============================")
    print("❌ TOOL ERROR CALLBACK")
    print(f"Time : {datetime.now()}")
    print(f"Tool : {tool.name}")
    print(f"Args : {args}")
    print(f"Error : {error}")
    print("==============================")

    return None