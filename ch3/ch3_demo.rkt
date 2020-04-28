(define (sqrt x)
    (define (goods-enough? guess)
    (< (abs (- (square guess) x)) 0.001))
    (define (improve guess)
    (average guess (/ x guess)))
    (define (sqrt-iter guess)
    (if (goods-enough? guess)
    guess
    (sqrt-iter (improve guess))))
    (sqrt-iter 1.0))

((lambda (x y z) (+ x y (square z)) 1 2 3))