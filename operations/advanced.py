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


# Find percentage of a number
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


# Logarith function
def log_base(value, base):
    try:
        value = float(value)
        base = float(base)
        if value <= 0 or base <= 0:
            return "Error: log undefined for non-positive numbers"
        return str(math.log(value, base))
    except Exception as e:
        return f"Error: {str(e)}"


# Find log 10
def log10(value):
    try:
        value = float(value)
        if value <= 0:
            return "Error: log10 undefined for non-positive numbers"
        return str(math.log10(value))
    except Exception as e:
        return f"Error: {str(e)}"


# ln(x) Natural logarithm
def ln(value):
    try:
        value = float(value)
        if value <= 0:
            return "Error: ln undefined for non-positive numbers"
        return str(math.log(value))
    except Exception as e:
        return f"Error: {str(e)}"
    