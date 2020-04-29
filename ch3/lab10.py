def eval(self, env):
    """
    >>> env = {
    ...     'a': Number(1),
    ...     'b': LambdaFunction([], Literal(0), {})
    ... }
    >>> Name('a').eval(env)
    Number(1)
    >>> Name('b').eval(env)
    LambdaFunction([], Literal(0), {})
    >>> print(Name('c').eval(env))
    None
    """
    "*** YOUR CODE HERE ***"
    return env.get(self.string, None)

def eval(self, env):
    """
    >>> from reader import read
    >>> new_env = global_env.copy()
    >>> new_env.update({'a': Number(1), 'b': Number(2)})
    >>> add = CallExpr(Name('add'), [Literal(3), Name('a')])
    >>> add.eval(new_env)
    Number(4)
    >>> new_env['a'] = Number(5)
    >>> add.eval(new_env)
    Number(8)
    >>> read('max(b, a, 4, -1)').eval(new_env)
    Number(5)
    >>> read('add(mul(3, 4), b)').eval(new_env)
    Number(14)
    """
    "*** YOUR CODE HERE ***"
    function = self.operator.eval(env)
    arguments = [operands.eval(env) for operands in self.operands]
    return function.apply(arguments)

def apply(self, arguments):
    """
    >>> from reader import read
    >>> add_lambda = read('lambda x, y: add(x, y)').eval(global_env)
    >>> add_lambda.apply([Number(1), Number(2)])
    Number(3)
    >>> add_lambda.apply([Number(3), Number(4)])
    Number(7)
    >>> sub_lambda = read('lambda add: sub(10, add)').eval(global_env)
    >>> sub_lambda.apply([Number(8)])
    Number(2)
    >>> add_lambda.apply([Number(8), Number(10)]) # Make sure you made a copy of env
    Number(18)
    >>> read('(lambda x: lambda y: add(x, y))(3)(4)').eval(global_env)
    Number(7)
    >>> read('(lambda x: x(x))(lambda y: 4)').eval(global_env)
    Number(4)
    """
    if len(self.parameters) != len(arguments):
        raise TypeError("Oof! Cannot apply number {} to arguments {}".format(
            comma_separated(self.parameters), comma_separated(arguments)))
    "*** YOUR CODE HERE ***"
    # 复制环境并更新
    lambda_env = self.parent.copy()
    # 不是很明白
    for para, arg in zip(self.parameters, arguments):
        lambda_env[para] = arg
    return self.body.eval(lambda_env)