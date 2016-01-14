(ns exercicio3.core
  (:gen-class))

(defn comprobar-parentesis [string]
	(def parentesis {\( \), \[ \], \{ \}})
	(defn aux [string, pia]
			(cond
				(empty? string) 
						(if (empty? pia)
								true
								false)
				(contains? parentesis (first string)) 
						(recur 	(rest string) (cons (get parentesis (first string)) pia))
				(= (first pia) (first string)) 
						(recur (rest string) (rest pia))
				:else 
						(recur (rest string) pia)))
	(print string) 
	(aux string [])
)
							
(defn -main
  []
  (println (comprobar-parentesis "((5+3)*2+1)"))
	(println (comprobar-parentesis "{[(3+1)+2]+}"))
	(println (comprobar-parentesis "(3+{1-1)}"))
	(println (comprobar-parentesis "[1+1]+(2*2)-{3/3}"))
	(println (comprobar-parentesis "(({[(((1)-2)+3)-3]/3}-3)"))
	(println (comprobar-parentesis "[2+3)"))
)
