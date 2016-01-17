#lang racket

;CREAR LISTA DE NÚMEROS ALEATORIOS

(define rango_random 50)
(define num_elementos_lista 20)

(define lista_entrada
  (map (lambda (x) (random rango_random))
       (make-list num_elementos_lista 0)))

;DEFINIMOS A FUNCIÓN ENCARGADA DE MOSTRAR OS ELEMENTOS REPETIDOS DA LISTA

(define (elementos_iguales lista)
    (define e (make-hasheq))
    (map (lambda(x) (hash-update! e x add1 0)) lista)
    (filter (lambda(z) (> (hash-ref e z) 1)) lista)
    )

(display lista_entrada)
(newline)
(elementos_iguales lista_entrada)

