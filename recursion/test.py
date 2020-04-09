def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

cascade(123)

'''
n = 1234
1
12
123
1234
123
12
1
'''
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

# def grow(n):
#     lambda n : f_then_g(grow, print, n // 10)

# def shrink(n):
#     lambda n : f_then_g(print, shrink, n // 10)

grow = lambda n : f_then_g(grow, print, n // 10)

shrink = lambda n : f_then_g(print, shrink, n // 10)

inverse_cascade(1234)