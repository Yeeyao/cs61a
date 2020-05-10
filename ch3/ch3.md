# ch3

- the design of interpreters and the computational process

- 这里才正式介绍 scheme 但是前面的 lab 就有练习了

## 3.2 functional programming

- scheme

- #f 仅仅这个是 false-y value 其他值都是 true-y value

- list procedure takes an arbitrary amount of arguments  

- = 仅仅可以用在比较数字 eq? 用在比较 two non-pairs equal? 可以比较 pairs 以及其他

## 3.3 exceptions

- any exception instance can be raised with raise statement

- 引发异常之后，后续的语句将不会被执行

- using try...except expression to handle an exception

- exception objects can have attributes

## 3.4 calculator

- expression trees

- parsing expressions

    - 从输入文本中生成语法树的过程，包含两个部分，一个词法(lexical) 分析器以及一个句法(syntactic) 分析器

    - 首先是词法分析器将输入字符串分解为 tokens 即语言的最小 syntactic unit

    - 然后，句法分析器从 tokens 队列中生成语法树

- read evaluate print loop

- 这里有个例子，连接两个 list，不断对第一个 list 进行 car 操作，然后 cons 操作，递归完成。这里的过程就先遍历第一个参数

## interpreters for language abstraction

- calculator interpreter 还不能解析所有的 Scheme 表达式，比如 quotation or dotted lists

- each Frame instance 表示一个环境，有一个 bindings 的字典

- 将一个程序类比成一个抽象的机器。然后 Scheme 解释器可以看作是一个特殊的机器

- eval procedure 允许计算一个已创建的表达式

- macros 是 procedure 接受表达式作为输入并返回 Scheme 表达式作为输出

    - define-macro Scheme 计算是先计算得到一个 macro 然后将 macro procedure 应用到操作数（这里操作数没有被计算）。

    - 最后从 macro procedure 返回结果

- a quote 可以让一个表达式不被计算 可以用 ' 或者 quote

- a quasiquotes 则让表达式部分不会被计算

## declarative programming

## sql

- 使用 || 将 select 中的字符串进行连接
