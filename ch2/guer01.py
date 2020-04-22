""" guer 01

## 1.1
```txt
lst = [1,2,3,4,5]
lst[1:3] [2,3]
lst[0:len(list)] [1,2,3,4,5]
lst[-4:] [2,3,4,5]
lst[3:] [4,5]
lst[1:4:2] [2,4] 1:4 隔 2 个取一个
lst[:4:2] [1,3]
lst[1::2] [2,4] 从 1 开始到最后，每隔两个元素取一个
lst[::-1] [5,4,3,2,1] 直接负数表示反序，前面省略默认是 0
lst + 100 invalid
```
"""
def map_mut(f, L):
    """
    >>> L = [1,2,3,4]
    >>> map_mut(lambda x:  x**2, L)
    >>> L
    [1, 4, 9, 16]
    """
    # [f(x) for x in L]
    # 这里需要手动改
    for i in range(len(L)):
        L[i] = f(L[i])

# 到达点 (m,n) 只有两条路径，即从 (m-1,n) 或者从 (m, n-1)
def paths(m, n):
    """
    >>> paths(2,2)
    2
    >>> paths(117,1)
    1
    """
    if m == 1 or n == 1:
        return 1
    return paths(m - 1, n) + paths(m, n - 1)

def merge(s1, s2):
    """ Merges two sorted lists
    >>> merge([1, 3], [2, 4])
    [1, 2, 3, 4]
    >>> merge([1, 2], [])
    [1, 2]
    """
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    elif s1[0] < s2[0]:
        return [s1[0]] + merge(s1[1:], s2)
    else:
        return [s2[0]] + merge(s2[1:], s1)
    