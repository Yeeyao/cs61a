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


def swap(arr, i1, i2):
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp

def dutchNatFlag(arr):
  
  low = 0
  mid = 0
  high = len(arr) - 1
  
  # one pass through the array swapping
  # the necessary elements in place
  while mid <= high:
    if arr[mid] == 0:
      swap(arr, low, mid)
      low += 1
      mid += 1
    elif arr[mid] == 2:
      swap(arr, mid, high)
      high -= 1
    elif arr[mid] == 1:
      mid += 1
      
  return arr
  
print dutchNatFlag([2,2,2,0,0,0,1,1]) 