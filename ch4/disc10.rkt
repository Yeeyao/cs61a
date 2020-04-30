(define (replicate x n)
  (if (= n 0) '()
      (cons(x (replicate x (- n 1)))))
)

(define (uncompress s)
  (if (null? s) s
      (my-append
       (replicate (car (car s)) (cdr (car s))) (uncompress (cdr s))))
)

(define (map fn lst)
  (if (null? lst) lst
      (cons (fn (car lst)) (map fn (cdr lst))))
)

(define (make-tree label branches) (cons label branches))
(define (label tree) (car tree))
(define (branches tree) (cdr tree))


(define (tree-sum tree)
  (+ (label tree) (sum (map sum (branches tree))))
)

(define (sum lst)
  (if (null? lst) 0
      (+ (car lst) (sum (cdr lst))))