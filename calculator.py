import math


def square_root(a: float) -> float:
    if a < 0:
        raise ValueError("input must be positive")
    return math.sqrt(a)


def hypotenuse(a: float, b: float) -> float:
    return math.hypot(a, b)


def add(a: float, b: float) -> float:
    return a + b


def sub(a: float, b: float) -> float:
    return a - b


def subtract(a: float, b: float) -> float:
    return sub(a, b)


def mul(a: float, b: float) -> float:
    return a * b


def multiply(a: float, b: float) -> float:
    return mul(a, b)


def div(a: float, b: float) -> float:
    if a == 0:
        raise ZeroDivisionError("division by zero")
    return b / a


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def log(a: float, b: float) -> float:
    if a <= 0 or a == 1:
        raise ValueError("invalid base for logarithm")
    if b <= 0:
        raise ValueError("invalid argument for logarithm")
    return math.log(b, a)


def logarithm(a: float, b: float) -> float:
    return log(a, b)


def exp(a: float, b: float) -> float:
    return a ** b


def exponent(a: float, b: float) -> float:
    return exp(a, b)


# end of file
