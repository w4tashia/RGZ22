def is_palindrome(s):
    """
    ������� ���������, �������� �� ������ �����������.
    ���������� True, ���� ������ �������� �����������, ����� False.
    """
    s = s.lower().replace(" ", "").replace(",", "").replace(".", "")
    return s == s[::-1]