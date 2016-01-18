#lang racket

;num + num -> vector de números aleatorios
(define (lista_entrada rang num)
  (build-list num (lambda(x) (random rang))))

;list -> lista de números repetidos
(define (elementos_iguales lista)
  (define d (make-hash))
  (map (lambda(x) (hash-update! d x add1 0)) lista)
  (filter (lambda(z) (> (hash-ref d z) 1)) lista)
  )

(define v (lista_entrada 20 20))

(displayln v)
(elementos_iguales v)