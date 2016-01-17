# -*- coding: utf-8 -*-

def eliminar_elementos_unicos(lista):

	#CREAMOS DICCIONARIO VACIO
	
	d = {}
	
	#RECORREMOS A LISTA DE NUMEROS
	
	for i in lista:
		#SE O NUMERO NON EXISTE COMO CLAVE DO DICCIONARIO CREASE CO VALOR 1,
		# SE EXISTE SUMASELLE 1.
		d[i] = d[i]+1 if i in d else 1
		#RECORREMOS A LISTA E DEVOLVEMOS AS CLAVES QUE TEÑAN UN VALOR DIFERENTE A 1
	return [i for i in lista if d[i] != 1]

lista_entrada = [1,2,3,1,3,23,1]
	
print "lista_entrada:", lista_entrada
print "lista saida:", eliminar_elementos_unicos(lista_entrada)