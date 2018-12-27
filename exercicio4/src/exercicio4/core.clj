(ns exercicio4.core
  (:gen-class))

(defn primo? [n]
	(empty? 
		(filter (fn [x] (= (rem n x) 0)) (range 2 n)))
)
				
(defn palindromo? [n]
 	(if (= (seq (str n)) (reverse (str n)))
 			true false))

(defn primo-palindromo+cercano [number]
	(defn aux [n]
		(if (and (primo? n) (palindromo? n))
				n
				(recur (inc n))))
	(aux (inc number)))

(def numbers-list [2 6 13 101 168 545 1003])

(defn -main
  []
  (println
  	(map 
  		(fn [x,n] (str "O primo palindromo superior e + cercano a " n " = " x "\n"))
  		(for [x numbers-list] (primo-palindromo+cercano x))
  		 numbers-list
  		)))
