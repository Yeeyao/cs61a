# lab

## Answer

### 1

- 23, 23, 6, 25

- big, huge, small nothin

- 2, 1, 0, -1

- positive...

- -12, -9, -6

### 2

- 13, 0, False, True

- 0, True, 0, 1, 15, 2

- True, 1, Error, False

### 3

- return x > 0 and y > 0

### 4

```python
def sum_digits(n):
    sum = 0
    while n > 0:
        add = n % 10
        sum += add
        n = n // 10
    return sum

def sum_digits(n):
    sum = 0
    while n > 0:
        sum, n = sum + n % 10, n // 10
    return sum
```

### 5

- 10, foo

- 1, 29, 29

### 6

```python
def falling(n, k):
    product = 1
    k = k + 1
    while k <= n:
        product, k = product * k, k + 1
    return product
```

### 7

```python
def double_eights(n):
    eight_count = 0
    while n > 0:
        if n % 10 == 8:
            eight_count += 1
        n = n // 10
    return eight_count > 0 and eight_count % 2 == 0
```