# -*- coding: utf-8 -*-

def parentOk(s):
	
	#CREASE UN DICCIONARIO USANDO COMO CLAVES OS PARENTESES ABERTOS E COMO VALORES OS CERRADOS DE CADA UN.
	
    pares = dict(["()", "{}", '[]'])
	
	#LISTA VACIA DONDE SE VAN ALMACENANDO OS PARENTESIS ABERTOS
	
    pia = []
	
	#RECORRESE O TEXTO
	
    for letra in s:
	
	#SE A LETRA É UN PARENTESIS ABERTO METESE NA LISTA <PIA>
	
        if letra in pares:
            pia.append(letra)
			
	#SE A LETRA É UN PARENTESIS CERRADO E ADEMÁIS NON HAI ELEMENTOS EN <PIA> OU 
	#	ÚLTIMO PARENTESE AÑADIDO A <PIA> NON CORRESPONDE CO PARENTESIS CERRADO
	#	QUERE DECIR QUE O TEXTO ESTA MAL.
	
        elif (letra in pares.values()
              and (not pia 
                     or pares[pia.pop()] != letra)):
            return False
	
	#SE <PIA> ESTA VACIO CANDO ACABA O BUCLE DEVOLVE <True>, EN CASO CONTRARIO DEVOLVE <False>
	
    return not pia
			
print "((5+3)*2+1)", "==", parentOk("((5+3)*2+1)")
print "{[(3+1)+2]+}", "==", parentOk("{[(3+1)+2]+}")
print "(3+{1-1)}", "==", parentOk("(3+{1-1)}")
print "[1+1]+(2*2)-{3/3}", "==", parentOk("[1+1]+(2*2)-{3/3}")
print "(({[(((1)-2)+3)-3]/3}-3)", "==", parentOk("(({[(((1)-2)+3)-3]/3}-3)")
print "2+3", "==", parentOk("[2+3)")