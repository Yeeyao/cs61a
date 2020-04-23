# container

- three native numeric types integers, real numbers, complex

- lists can gbe added and multiplied by integers

- range, with one argument, begins with 0, 前闭后开

- membership and slicing

- tree and linked list

## object

- have attributes using dot syntax to designate an attribute

## dictionary

- kv pairs

- dict([(a,1)]) 可以将 list 转换为 dictionary

## local state

- nonlocal statement 起到类似访问外部变量并改变其数值的作用

- 赋值语句创建新的绑定或者对已经存在的变量名字重新绑定

- python 名字查找中，在一个函数体内，一个名字的所有实例必须引用在同一个 frame 中

- 需要注意变量生效的 frame

## iterators

- an iterator 维护一个在一个序列中保存其位置的局部状态

- 对一个 iterator 调用 iter() 将返回该 iterator

- 可以实现 lazy generation

## generators

- 允许对任何序列进行定义 iterations

- yield statement 表示我们在定义一个 generator function，调用时，将返回一个 generator

- 对该 generator 调用 next 函数时，generator function 将被执行到下一个 yield 前并返回值

- 使用 yield statements来返回一个系列的元素

## dispatch dictionaries

- By storing the balance in the dispatch dictionary we avoid the need for nonlocal statements

## propagating constraints

- 类似 SICP 中的例子

## implicit sequences

- 数组不是整个一直存在于内存中，而是根据需要来计算

## python streams

- 可以用来表示 sequential data implicitly is a lazily computed linked list

- the rest of stream is a stream, only computed when it is looked up

    - stores a function(_rest) that computes the rest of the stream

    - 上述下划线表示该函数无法被直接访问

## OOP

- class self and method, when calling methods, the object 将 bound to self

- dot expression and getattr/hasattr function

- function and bound method

- class name 使用驼峰命名法，method 用下划线连接

- underscore 开头的 attribute name 只能被 class 的 method 访问

- class attributes 同个 class 所有的 instance 都可以访问

- 修改 class 的 attributes 将对所有的 instance 的对应 attribute 进行修改。修改 instance 的 class attribute 将不会影响其他的 instance 的该值

- inheritance 仍然可以在子类中调用父类的方法

- multiple inheritance

- the Python object system is designed to make data abstraction and message passing both convenient and flexible

## 2.7 object abstraction

- 泛型，多态函数

- string conversion str() repr() function 后者调用对象的 __repr__ 函数

- 创建一个 object 时，将自动调用 __init__ 函数，判断 bool 值时，将调用对象的 __bool__ 函数

- 调用 len() 函数将自动调用对象的 __len__ 函数

- @property decorator 允许函数不需要调用语法就可以被调用

- complex number using interfaces and message passing 实现泛型函数

    - 定义一个类，然后多个不同复数表示的子类以及转换定义

- type dispatching 基于参数类型选择合适的行为来实现跨类型的操作

    - 使用 isinstance 函数判断参数类型进行分派

    - 多个不同类型之间数据操作的处理 先判断参数的类型，如果相同就直接使用内置的操作，如果不同，根据类型进行操作函数的分派

- coercion 针对不同类型数据间的一些操作，可以定义自己的转换函数，将一个数据类型转换然后再执行操作。

    - 一些复杂的操作可能需要将两个参数转换成第三种类型

    - 转换类型有信息丢失的 drawback
