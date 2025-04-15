import math


def square(number):
    # Allow square calculations
    try:
        return str(float(number) ** 2)
    except Exception:
        return "Error"


def square_root(number):
    # calculate square root of numbers
    try:
        num = float(number)
        return str(math.sqrt(num) if num >= 0 else "Error: √(-)")
    except Exception:
        return "Error"


def percentage(number):
    # Convert numbers to percenbtage
    try:
        return str(float(number) / 100)
    except Exception:
        return "Error"