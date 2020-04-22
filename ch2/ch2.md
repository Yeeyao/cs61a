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

- 使用 yield statements来返回一个系列的元素

- 控制 generator function, 当调用 next 函数时，generator function 将被执行到 yield 前并返回值

## dispatch dictionaries

- By storing the balance in the dispatch dictionary we avoid the need for nonlocal statements

## propagating constraints

- 类似 SICP 中的例子
