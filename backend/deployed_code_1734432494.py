def factorial(n):
    if n < 0:
        raise ValueError("Факториал отрицательных чисел не определён.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)