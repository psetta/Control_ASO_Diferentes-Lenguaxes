#lang racket

;num + num -> lista de números aleatorios
(define (lista_entrada rang num)
  (for/list ([i (in-range num)]) (random rang)))


;list -> lista de números repetidos
(define (elementos_iguales lista)
  (define d (make-hash))
  (map (lambda(x) (hash-update! d x add1 0)) lista)
  (filter (lambda(z) (> (hash-ref d z) 1)) lista)
  )

(elementos_iguales (lista_entrada 100 100))