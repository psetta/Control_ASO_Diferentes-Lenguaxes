# -*- coding: utf-8 -*-

import re

def sacar_correos(string):
	
	#EMPREGAMOS A EXPRESIÓN REGULAR PARA ENCONTRAR CORREOS ELECTRÓNICOS
	
	#\w 		--> caracter (poden ser números, guións, etc)
	#\. 		--> punto "."
	#| 			--> OR
	#+ 			--> Un ou máis elementos precedentes
	#{min,max}	--> número mínimo e máximo do elemento precendente

	return re.findall("[\w|\.]+@[\w|\.]+\.\w{2,4}",string)
	
texto_de_proba = """Welcome to RegExr v2.0 by gskinner.com!
Edit the Expression & Text to see matches.
Sample text for testing:
abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 _+-.,!@#$%^&*();\/|<>"'
12345 -98.7 3.141 .6180 9,000 +42
555.123.4567	+1-(800)-555-2468
foo@demo.net	bar.ba@test.co.uk
www.demo.com	http://foo.co.uk/
http://regexr.com/foo.html?q=bar
carlos.21@gmail.com carlos.augusto_21@asir.iessanclemente.net"""


print "TEXTO:\n"+ texto_de_proba+"\n"
print "correos:", sacar_correos(texto_de_proba)