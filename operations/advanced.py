import math


def square(value):
    # Allow square calculations
    try:
        return str(float(value) ** 2)
    except ValueError:
        return f"Error"


# Calculate square root
def square_root(value):
    try:
        num = float(value)
        if num < 0:
            return "Error"
        return str(round(math.sqrt(num), 6))
    except ValueError:
        return "Error"


def percentage(value):
    try:
        num = float(value)
        return str(round(num / 100, 6))
    except ValueError:
        return "Error"


def exponentiate(base, exponent):
    """Find the exponent of a number"""
    try:
        result = float(base) ** float(exponent)
        return str(result)
    except ValueError:
        return "Error"