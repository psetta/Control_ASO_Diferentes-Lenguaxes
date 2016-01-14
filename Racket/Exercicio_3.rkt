#lang lazy

(define (comprobar-parentesis texto)
  (define parentesis (hash #\( #\) #\[ #\] #\{ #\}))
  (define (aux lista pila)
    (cond
      ([empty? lista]
       (if (empty? pila) #t #f))
      ([member (car lista) (hash-keys parentesis)]
       (aux (cdr lista) (cons (car lista) pila)))
      ([member (car lista) (hash-values parentesis)]
       (cond
         ([empty? pila] #f)
         (else
          (cond
            ([equal? (hash-ref parentesis (car pila)) (car lista)]
             (aux (cdr lista) (cdr pila)))
            (else #f)))))
      (else
       (aux (cdr lista) pila))))
  (display texto)
  (aux (string->list texto) empty))

(comprobar-parentesis "((5+3)*2+1)")
(comprobar-parentesis "{[(3+1)+2]+}")
(comprobar-parentesis "(3+{1-1)}")
(comprobar-parentesis "[1+1]+(2*2)-{3/3}")
(comprobar-parentesis "(({[(((1)-2)+3)-3]/3}-3)")
(comprobar-parentesis "[2+3)")