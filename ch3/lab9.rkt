(define (over-or-under a b)
    (cond 
        [(> a b) (1)]
        [(= a b) (0)]
        [else -1]
    )
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0

; if empty return '() if true, cons else call cdr
(define (filter-lst fn lst)
    (cond 
        ((null? lst) '())
        ((fn (car lst)) (cons (car lst) (filter-lst fn (cdr lst))))
        (else (filter-lst fn (cdr lst))))
)

(define (even? x)
  (= (modulo x 2) 0))

(define (make-adder n)
  (lambda (x) (+ n x))
)

(define adder (make-adder 5))

(define lst
  (cons (cons 1 '())
        (cons 2
                (cons(cons 3(cons 4 '()))   
                     (cons 5 '()))))
)

(define (composed f g)
  (lambda x (f (g x)))
)

(define (remove item lst)
  (filter-lst (lambda (x) (not (= x item))) lst)
)

(define (remove item lst)
    (cond 
        ((null? lst) '())
        ((not(= item (car lst))) (cons (car lst) (remove item (cdr lst))))
        (else (remove item (cdr lst))))
)

; 使用 filter 每次过滤掉等于列表第一个元素的值
(define (no-repeat s)
  (if (null? s) s
      (cons (car s)
            (no-repeat (filter (lambda (x) (not (= (car s) x))) (cdr s)))))
)

;这个还没有看懂
(define (substitute s old new)
  (cond ((null? s) nil)
        ((pair? (car s)) (cons (substitute (car s) old new)
                               (substitute (cdr s) old new)))
        ((equal? (car s) old) (cons new
                                    (substitute (cdr s) old new)))
        (else (cons (car s) (substitute (cdr s) old new))))
)

(define (sub-all s olds news)
  (if (null? olds)
    s
    (sub-all (substitute s (car olds) (car news))
             (cdr olds)
             (cdr news)))
)