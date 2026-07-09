def calculate(
    num1: float,
    operator: str,
    num2: float,
) -> dict:
    """
    Performs a basic mathematical calculation.
    """

    operations = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2 if num2 != 0 else "Cannot divide by zero",
    }

    return {
        "expression": f"{num1} {operator} {num2}",
        "result": operations.get(operator, "Invalid operator"),
    }