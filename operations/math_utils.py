def nth_root(base: float, n: float) -> float:
    """
    Calculate the nth root of a number.
    
    :param base: The number to find the root of.
    :param n: The degree of the root.
    :return: The nth root of the base.
    """
    if n == 0:
        raise ValueError("Root degree cannot be zero.")
    if base < 0 and n % 2 == 0:
        raise ValueError("Cannot compute even root of a negative number.")
    return base ** (1.0 / n) 
    