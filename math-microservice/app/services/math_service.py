# Placeholder content for math_service.py
# app/services/math_service.py
def calculate_power(base: int, exp: int) -> int:
    return base ** exp


def calculate_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Negative input")
    return 1 if n in (0, 1) else n * calculate_factorial(n - 1)


def calculate_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Negative input")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
