from datetime import datetime


def get_current_time() -> dict:
    """
    Returns the current local date and time.
    """

    return {
        "current_time": datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    }