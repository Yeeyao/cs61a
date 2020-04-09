# week1

## function

- abstractions

- do exactly one job, a short name imply its job.

- don't repeat yourself.

### function name

- 出现在两个地方，一个是frame，另一个是函数本身。前者只是函数绑定到具体函数的名字，后者是函数的intrinsic name

- 这里函数签名的定义是函数形参的描述

- 使用一个用户定义的函数将引入第二个local frame，仅仅该函数可以访问

    - 使用时将在一个新的local frame中先将参数绑定到函数的形参。之后在该frame中开始的环境下执行该函数体

- 函数抽象

    - 函数作为一层抽象，其实现需要隐藏细节，对于调用者来说，应该是一个黑箱

    - 这里提出函数抽象三个属性

        - domain: the set of args it can take

        - range: the set of values it can return

        - behaviour: I/O's relationship

### Documentation

- A function definition includes documentation describing the funtion, called docstring, which must be indented with the function body. Triple quoted.

- call help with the name of a function as an argument, you see its docstring

```python
"""Compute the pressure in pascals aof an ideal gas."""
>>>help(pressure)
```

### Default Argument Values

- argumnets with default values are optional.

- Binding arguments when defining a function.

### testing

- 测试函数的行为是否符合预期

- 测试是系统执行上述验证的一种机制。测试典型地使用另外一个函数来一次或者多次调用被测试函数进行，最终的返回值用来与期望的结果进行比较。当然，将使用特定的参数值来进行测试。

- 测试也起到文档的作用，它们延时可如何调用一个函数以及给出合适的参数值

#### Assertions

- 程序员使用assert语句来验证期望。其中后面的表达式需要返回一个布尔值，如果验证通过，将打印最后的文本。

- 如果表达式返回true，则执行一个assert statement将不会有作用，如果返回false则会产生中断执行的error。

#### Doctests

- python提供一种直接在一个函数的docstring中存放简单的test的方法。

    - 第一行是函数描述，接着是一个空行，接着是参数以及行为的细节描述。
  
    - 同时，docstring需要包含一个调用函数的语句(interactive session)。

        - 该interaction将在doctest module中被验证

```python
>>> assert fib(8) == 13, 'The 8th Fibonacci number should be 13'
```

## condition/control

- Each clause is considered in order.

- Evaluate the header's expression.

- If it's a true value, execute the suite. Then skip over all subsequent clauses in the conditional statement.

- false values in Python: False, 0, '', None

- All of the expressions to the right of = are evalutated before any bindings takes place.

```python
if <expression>:
    <suite>
elif <expression>:
    <suite>
else:
    <suite>
```

### none

- None是一个特殊值，在python中表示nothing

- 一个没有显示返回的函数将返回None

- side effect: 调用一个函数后的结果

- Expressions 表达式：程序中用来求值

- Statements 语句：用于执行某些行为，比如赋值和def statements

### Boolean Expression

- and or not

- and以及or都使用短路求值

## alternative

- data 8 CS C8 [data8](http://data8.org/)

## Environment diagrams

- 一种可视化工具来记录一个计算机程序的绑定和状态

- 概念化的，便于调试

- An environment is a series of frames

- 调用函数的时候，the parent是函数定义的地方。所以，调用函数的时候，其创建的frame的parent总是函数定义的地方

- name binding对于多个同名的变量，总是取最后一个binding，所以需要注意顺序的影响

- An intrinsic name and its parent give an unique function object

- 函数的 environment 中的 parent 是其定义所在的上下文

### Frame

- 记录变量到值的绑定

    - 每个表达式的调用都将有一个对应的frame

- Global 全局的frame是the starting frame

    - 不会对应一个特定的调用表达式

- parent frames

    - 一个函数的parent是其被定义的frame

    - 当你在当前的frame中无法找到一个变量，你将要查找其parent并继续查找，如果一直找不到则NameError（查找在global frame中停止）

- call expressions create new frames

### lambda expression

- 与def都创建了新的函数，但是lambda创建匿名函数

- the parent frame都是类似

- 都将函数绑定到一个名字，其中lambda是符号

    - 同时，python将lambda表达式的行号绑定到lambda的函数体

    - 所有的lambda表达式的intrinsic name都是相同的，不同的只是他们定义的代码位置不同

- def给定函数一个intrinsic name

### 高阶函数

- 可以表达通用的计算方法

- 将一个函数作为一个参数值或者返回值是一个函数

- 处理函数的函数被称为高阶函数

- local def statement 仅仅影响local frame.

- the inner functions have access to the names in the environment where they are defined.

- 函数是第一类的, Functions are first-class。python中函数可以像对待值一样处理

    - they can be manipulated as values

- currying

    - 使用函数以及其返回的函数来处理，其中参数通过函数间传递，比如要实现f(x, y)，可以定义函数g使得g(x)(y)等价于f(x, y)

    - 将一个多参数函数转换为单一参数的高阶函数

- 高阶函数允许我们进行更多的抽象

- 作为程序员，我们应该发现我们程序中的潜在的抽象，在此基础上编写程序并使它们通用化来获得更加强大的抽象

- 高阶函数的意义是它们允许我们在我们的程序语言中直观地表达抽象。使得它们可以像其他计算元素一样被利用起来

- 一般情况下，程序语言将对它的计算元素能够被使用的方式施加一定限制。其中有着最少限制的元素被称为有first-class status.

    - 它们可以被绑定名字

    - 它们可以作为参数传递给函数

    - 它们可以作为函数的返回值

    - 它们可以包含在数据结构当中

- Python给予函数 full first-class status,并且获得了巨大的表达能力

- Decorators

    - 跟踪函数执行 @trace
