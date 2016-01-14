#lang racket

;CREAR LISTA DE NÚMEROS ALEATORIOS

;ESTE É MÁIS RÁPIDO QUE O ANTERIOR

(define rango_random 3333333333)
(define num_elementos_lista 1000000)

(define lista_entrada
  (map (lambda (x) (random rango_random))
       (make-list num_elementos_lista 0)))

;DEFINIMOS A FUNCIÓN ENCARGADA DE QUITAR ELEMENTOS ÚNICOS DUNHA LISTA

(define (elementos_iguales lista)
  (define d (make-hash))
  (map (lambda(x) (hash-update! d x add1 0)) lista)
  (filter (lambda(z) (> (hash-ref d z) 1)) lista)
  )

(elementos_iguales lista_entrada)
