def is_palindrome(s):
    """
    Функция проверяет, является ли строка палиндромом.
    Возвращает True, если строка является палиндромом, иначе False.
    """
    s = s.lower().replace(" ", "").replace(",", "").replace(".", "")
    return s == s[::-1]