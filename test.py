def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        while n > 1:
            a, b = b, a + b
            n -= 1
    return b

def count_up(n):
    """
    >>> count_up(1)
    1
    >>> count_up(2)
    1
    2
    >>> count_up(3)
    1
    2
    3
    >>> count_up(4)
    1
    2
    3
    4
    """
    if n == 1:
        print(n)
    else:
        count_up(n - 1)
        print(n)

def sum_digits(n):
    """calculates the sum of the digits `n`.
    >>> sum_digits(9)
    9
    >>> sum_digits(19)
    10
    >>> sum_digits(2019)
    12
    """
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)

def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

def cascade2(n):
    print(n)
    if n >= 10:
        cascade(n // 10)
        print(n)