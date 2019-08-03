# def square_root_update(x, a):
#     return (x + a / x) / 2

# def cube_root_update(x, a):
#     return (2 * x + a / (x * x)) / 3 

# def sauqre_root(a):
#     def update(x):
#         return square_root_update(x * x, a)
#     def close(x):
#         return approx_eq(x * x, a)
#     return improve(update, close)

# def cube_root(a):
#     return improve(lambda x: cube_root_update(x, a),
#                     lambda x: approx_eq(x * x * x, a))
                
def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

def power(x, n):
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product

def root(n, a):
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n - 1)
    return find_zero(f, df)

# def square_root(a):
#     def f(x):
#         x * x - a
#     def df(x):
#         2 * x
#     return find_zero(f, df)

# def cube_root(a):
#     return find_zero(lambda x: x * x * x - a, 
#                         lambda x: 3 * x *x)

def improve(update, close, guess = 1, max_update = 100):
    k = 0
    while not close(guess) and k < max_update:
        guess = update(guess)
        k = k + 1
    return guess

def approx_eq(x, y, tolerance = 1e-15):
    return abs(x - y) < tolerance
