(ns exercicio1.core
  (:gen-class))

 (def lista_entrada [1 2 3 4 5 2 4 4 6])
 ;(def lista_entrada (repeatedly 10 #(rand-int 9)))

 (defn actualizar_dict [dict lista]
 		(if (empty? lista)
 				dict
 				(recur 
 							(update dict (first lista) inc) 
 							(rest lista))))

 (defn elementos_coincidentes [list]
 		(def dict (actualizar_dict 
 											(zipmap list (repeat 0)) 
 											list))
 		(filter 
 			(fn [x] (> (get dict x) 1)) 
 			list))

(defn -main
  	[]
  	(println "lista_entrada:" lista_entrada)
  	(println "elementos_coincidentes:" (elementos_coincidentes lista_entrada))
  	)