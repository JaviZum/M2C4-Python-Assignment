M2C4 Python Assignment

#Exercise 1

lista = ["pepe", "juan", "luis", "antonio", "jon"] #lista

tupla = ("receta de manzana", "ingredientes: manzanas, azucar", "se cuecen las manzanas y se echa el azucar") #tupla

flotante = 13.95 #float

numero = -5 #integer

from decimal import Decimal #importada en este punto exprofeso

numero_decimal = Decimal(3.14)

espasa = {"ar": "armario", "em": "empotrado", "mur": "murcielago"}



#Exercise 2

import math #importada en este punto exprofeso

redondeo = math.ceil(flotante) #redondeo hacia arriba



#Exercise 3
    
raiz = math.sqrt(flotante) #raiz cuadrada del numero flotante. 13.95



#Exercise 4
#Anulada esta forma, por indicar el instructor que la que no esta comentada es la mejor práctica.
#primer_elemento_diccionario = list(espasa.items())[0]  #primer key/elemento del diccionario
# Ejemplo de selección del primer elemento del diccionario (ALTERNATIVA INSTRUCTOR)
#espasa = {"ar": "armario", "em": "empotrado", "mur": "murcielago"}
primer_elemento_diccionario = next(iter(espasa.items()))
print(primer_elemento_diccionario)


#Exercise 5
segundo_elemento_tupla = tupla[1] #asignamos a segundo_elemento_tupla el segundo elemento de la tupla



#Exercise 6
lista.append("delfin") #Añado "delfin" al fin.



#Exercise 7
lista[0]="pepa" #Cambio a pepe por pepa



#Exercise 8
orden = lista.sort() #ordenada la lista. Aqui aprendi que sort se aturulla con las mayúsculas... XD



#Exercise 9
tupla += ("autor",) #se añade autor a la tupla reasignada -que no original-.
print(tupla)
