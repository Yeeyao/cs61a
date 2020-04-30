(define (sum-satisfied-k lst f k)
  (define (ssk lst k rl)
    (cond ((null? lst) 0)
          ((= k 0) rl)
          ((f (car lst))
            (ssk (cdr lst) (- k 1) (+ (car lst) rl)))
          (else (ssk (cdr lst) k rl))))
  
  (ssk lst f k 0)
)

(define (remove-range lst i j)
  (define (rr lst index rl)
    (cond
      ((> index j)
       (append rl lst))
      ((>= index i)
       (rr (cdr lst) (+ index 1) rl))
      (else
       (rr (cdr lst) (+ index 1) (append  rl (list (car lst)))))))
 (rr lst 0 '())
)

; 没懂
(define-macro (when condition . exprs)
  (list 'if condition (cons 'begin exprs) ''okay))

(define-macro (when condition . exprs)
  `(if , condition ,(cons 'begin exprs) 'okay))