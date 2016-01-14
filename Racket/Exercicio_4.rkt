#lang racket

(define (primo? numero)
  (not
   (for/or ([i (range (integer-sqrt numero) 1 -1)])
     (= (remainder numero i) 0))))

(define (palindromo? numero)
  (equal? (string->list (number->string numero))
          (reverse (string->list (number->string numero)))))

(define (primo-palindromo+proximo n)
  (define numero (add1 n))
  (cond
    ([and (primo? numero) (palindromo? numero)] numero)
    (else
     (primo-palindromo+proximo (add1 n)))))

(define lista_numeros (list 2 6 13 101 168 545 1003))

(for ([i lista_numeros])
  (display (list "O primo palindromo + cercano a" i "=" (primo-palindromo+proximo i)))
  (newline))

