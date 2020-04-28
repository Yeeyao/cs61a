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
