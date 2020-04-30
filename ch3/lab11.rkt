!(define (flatmap f x)
  (define (h z x)
    (if (null? x)
        z
        (h (append z (f (car x))) (cdr x))))
  (h nil x))

(define (flatmap f x)
  (cond ((null? x) '())
        (cons (f (car x)) (flatmap f (cdr x))))
)

(define (expand lst)
  flatmap(lambda (x)
           (cond
             ((equal x 'x) '(x r y f r))
             ((equal y 'y) '(l f x l f))
             (else (list x))))
)

(define (interpret instr dist)
  (if (null? instr)
      nil
      (begin (define inst (car instr))
             (cond
               ((equal? 'f inst) (fd dist))
               ((equal? 'r inst) (rt 90))
               ((equal? 'l inst) (lt 90)))
             (interpret (cdr instr) dist)))
)

(define (apply-many n f x)
  (if (zero? n)
      x
      (apply-many (- n 1) f (f x))))

(define (dragon n d)
  (interpret (apply-many n expand '(f x)) d))