import math


def _to_float(value):
    try:
        return float(value), None
    except (ValueError, TypeError):
        return None, "Error"


def square(value):
    num, err = _to_float(value)
    if err:
        return err
    return str(round(num ** 2, 6))


def square_root(value):
    num, err = _to_float(value)
    if err or num < 0:
        return "Error"
    return str(round(math.sqrt(num), 6))


def percentage(value):
    num, err = _to_float(value)
    if err:
        return "Error"
    return str(round(num / 100, 6))


def exponentiate(base, exponent):
    base_num, err1 = _to_float(base)
    exp_num, err2 = _to_float(exponent)
    if err1 or err2:
        return "Error"
    return str(round(base_num ** exp_num, 6))


def log_base(value, base):
    val_num, err1 = _to_float(value)
    base_num, err2 = _to_float(base)
    if err1 or err2 or val_num <= 0 or base_num <= 0:
        return "Error"
    try:
        return str(round(math.log(val_num, base_num), 6))
    except Exception:
        return "Error"


def log10(value):
    num, err = _to_float(value)
    if err or num <= 0:
        return "Error"
    try:
        return str(round(math.log10(num), 6))
    except Exception:
        return "Error"


def ln(value):
    num, err = _to_float(value)
    if err or num <= 0:
        return "Error"
    try:
        return str(round(math.log(num), 6))
    except Exception:
        return "Error"


def nth_root(num, value):
    """
    Calculate the nth root of a value.
    Args:
        num: The root value (e.g., "3").
        value: The base number (e.g., "27")
    Returns:
        str: The nth root result or "Error" if invalid.
    """
    try:
        num = float(num)
        value = float(value)
        if num == 0:
            return "Error"
        if value < 0 and int(num) % 2 == 0:
            return "Error"
        result = value ** (1.0 / num)
        return str(round(result, 10))
    except Exception:
        return "Error"
