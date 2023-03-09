"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    Performs addition between a and b

    Parameters
    ----------
    a : int
    b : int

    Returns
    -------
    int
        Sum of a and b.
    """
    return a+b


def simple_sub(a,b):
    """
    Performs subtraction between a and b

    Parameters
    ----------
    a : int
    b : int

    Returns
    -------
    int
        The difference between a and b.
    """
    return a-b

def simple_mult(a,b):
    """
    Performs multiplication between a and b.

    Parameters
    ----------
    a : int
    b : int

    Returns
    -------
    int
        The product for a * b
    """
    return a*b

def simple_div(a,b):
    """
    Performs division between a and b

    Parameters
    ----------
    a : int,
        numerator
    b : int
        denominator
    Returns
    -------
    int
        quotient between a and b

    """
    return a/b

def poly_first(x, a0, a1):
    """
    Calculates the y-value on a straight line following
    a linear equation: a0x+a1

    Parameters
    ----------
    x : int
        x value of desired point
    a0 : int
        slope of the line
    a1 : int
        value where the line cuts the Y-axis

    Returns
    -------
    The Y-value of the linear equation
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    Calculates the Y value for a second grade polynomial
    with the following form: a2x² + c where c = a0x+a1

    Parameters
    ----------
    x : int
        x value of the desired point
    a0 : int
    a1 : int
    a2 : int

    Returns
    -------
    Y-value of the desire point on the second grade polynomial

    """
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
