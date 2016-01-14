# -*- coding: utf-8 -*-

import math

#CREAMOS UNHA FUNCIÓN PARA COMPRABAR SE UN NÚMERO É PRIMO

def primo(numero):
	for n in range(2,int(math.sqrt(numero))+1):
		
		#COMPROBAMOS SE O NÚMERO É DIVISIBLE POR ALGÚN NÚMERO QUE NON SEXA 1 NIN EL MESMO
		
		if numero % n == 0:
		
			#EN CASO DE QUE O SEXA O NÚMERO NON É PRIMO
			
			return False
	
	#NO CADO DE QUE ACABE O BUCLE O NÚMERO TEN QUE SER PRIMO
	
	return True

def primo_palindromo_cercano(numero):
	numero_pp = numero+1
	
	#CREAMOS UN BUCLE WHILE QUE COMPROBE SE O NÚMERO É PALINDROMO E PRIMO
	
	while not (primo(numero_pp) and str(numero_pp) == str(numero_pp)[::-1]):
	
		#SE NON O É SUMAMOS 1 AO NÚMERO
		
		numero_pp += 1
		
	return numero_pp
	
#PROBAMOS A PASARLLE UNHA LISTA DE NÚMEROS A FUNCIÓN
		
lista_numeros = [2,6,13,101,168,545,1003]

for n in lista_numeros:
	print u"O primo palindromo máis cercano a", n, u"é <"+ str(primo_palindromo_cercano(n))+">"