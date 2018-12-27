(ns exercicio2.core
  (:gen-class))

(def texto
  "Welcome to RegExr v2.0 by gs
   Edit the Expression & Text to see matches.
   Sample text for testing:
   abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
   0123456789 _+-.,!@#$%^&*();/|<>
   12345 -98.7 3.141 .6180 9,000 +42
   555.123.4567	+1-(800)-555-2468
   foo@demo.net	bar.ba@test.co.uk
   www.demo.com	http://foo.co.uk/
   http://regexr.com/foo.html?q=bar
   carlos.21@gmail.com carlos.augusto_21@asir.iessanclemente.net")

(defn show_emails [string]
	(re-seq #"[\w|\.]+@[\w|\.]+\.\w{2,4}" string))


(defn -main
  []
  (println (show_emails texto))
 )
