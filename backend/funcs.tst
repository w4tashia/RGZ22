def find_prime_factors(n):
    """
    Функция находит все простые множители числа n.
    """
    if n <= 1:
        return []

    factors = []
    # Проверяем делимость на 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Проверяем делимость на все нечетные числа от 3 до sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # Если n больше 2, то оно само является простым числом
    if n > 2:
        factors.append(n)
    
    return factors

12 2 2 3
15 3 5
100 2 2 5 5
45 3 3 5
77 7 11

def factorial(n):
    if n < 0:
        raise ValueError("Факториал отрицательных чисел не определён.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

5 120
0 1
1 1
2 2
3 6
4 24

def is_prime(n):
    """
    Функция проверяет, является ли число простым.
    Возвращает True, если число простое, иначе False.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

1 0
2 1
3 1
4 0
5 1
9 0
11 1
16 0


def fibonacci(n):
    """
    Функция возвращает n-е число Фибоначчи.
    Числа Фибоначчи начинаются с 0, 1, 1, 2, 3...
    """
    if n < 0:
        raise ValueError("Фибоначчи определены только для неотрицательных чисел.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

0 0
1 1
2 1
3 2
4 3
5 5
6 8
7 13
8 21


def is_palindrome(s):
    """
    Функция проверяет, является ли строка палиндромом.
    Возвращает True, если строка является палиндромом, иначе False.
    """
    s = s.lower().replace(" ", "").replace(",", "").replace(".", "")
    return s == s[::-1]

"madam" 1
"racecar" 1
"hello" 0
"Was it a car or a cat I saw" 1
"No lemon, no melon" 1
"test string" 0
"12321" 1
"12345" 0


def sort_array(arr):
    """
    Функция возвращает отсортированный массив.
    """
    return sorted(arr)


"3 1 2" 1 2 3
"10 5 2 8" 2 5 8 10
"100 1 50 25" 1 25 50 100
"9 8 7 6 5 4 3 2 1" 1 2 3 4 5 6 7 8 9
"5 5 5 5" 5 5 5 5
