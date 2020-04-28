(define (factorial x)
  (if (equal? x 0) 1 (* x (factorial (- x 1))))
)

(define (fib n)
  (cond
    [(equal? n 0) 0]
    [(equal? n 1) 1]
    [else (+ (fib (- n 1)) (fib (- n 2)))]
  )
)

(define (fib n)
    (if (<= n 1)
        n
        (+ (fib (- n 1)) (fib (- n 2))))
)

; 所以这个就是所说的，append 是相反的反向的处理逻辑
(define (my-append a b)
  (if (null? a) b (cons (car a) (my-append (cdr a) b)))
)