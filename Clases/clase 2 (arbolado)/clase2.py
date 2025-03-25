import csv

#1

nombre_archivo = 'arbolado.csv'

def leer_parque(nombre_archivo, parque):
    
    with open(nombre_archivo, 'r', encoding= 'utf-8') as file:
        filas = csv.DictReader(file)
        park = []
        for fila in filas:
            if fila["espacio_ve"] == parque:
                fila["altura_tot"] = float(fila["altura_tot"])
                fila["inclinacio"] = float(fila["inclinacio"])
                park.append(fila)
                    
    return park

#print(len(general_paz_Arboles))        

#2

#print(general_paz_Arboles)    

general_paz_Arboles = leer_parque(nombre_archivo, 'GENERAL PAZ')

def especies(lista_arboles):
    
    treeSet = set()     #Con Set me garantizo que no haya repetidos. Creo un conjunto desordenado
    
    for categoria in lista_arboles:
        treeSet.add(categoria["nombre_com"])
            
    return treeSet

#print(especies(general_paz_Arboles))

#3


# Tengo la lista, usando leer parque
# clasifico las especies, usando la funcion especies
# recorro la lista viendo cada especie y agregandola al diccionario



def contar_ejemplares(lista_arboles):
    
    contadorArboles_Especie = {}
    
    for arbol in lista_arboles:
        
        especie = arbol["nombre_com"]
        
        if especie in contadorArboles_Especie:    
            contadorArboles_Especie[especie] += 1
        else:
           contadorArboles_Especie[especie] = 1 
        
    return contadorArboles_Especie
            
centenario_Arboles = leer_parque(nombre_archivo, 'CENTENARIO')
losAndes_Arboles = leer_parque(nombre_archivo, 'EJERCITO DE LOS ANDES')  # 1 Tilo en vez de 3

#print(contar_ejemplares(centenario_Arboles)) # Ambos Centenario y General Paz son correctos


#4

# Dada una lista general y una especie especifica de un arbol, se devuelva la altura maxima y la promedio
# - modifico leer_parque para convertir la altura en float y hacer cuentas matematicas mas simples
# - creo una lista y elijo la especie
# - leo lista_arboles y agrego todos los floats a la lista nueva
# - calculo el promedio y altura maxima


def obtener_alturas(lista_arboles, especie):
    
    height_list = []
    
    for arbol in lista_arboles:
        
        alturaIndividual = arbol["altura_tot"]
        
        if arbol["nombre_com"] == especie:
            height_list.append(alturaIndividual)
            
    return height_list

#print(obtener_alturas(general_paz_Arboles, 'Jacarandá'))
#print(len(obtener_alturas(general_paz_Arboles, 'Jacarandá')))    #20 

def arbolMasAlto_Especie(lista_arboles, especie):
    
    return max(obtener_alturas(lista_arboles, especie))
    
def promedioArbol_Especie(lista_arboles, especie):
    
    return round(sum(obtener_alturas(lista_arboles, especie)) / len(obtener_alturas(lista_arboles, especie)),2)
    

#print(arbolMasAlto_Especie(general_paz_Arboles, 'Jacarandá')) # 16
#print(arbolMasAlto_Especie(centenario_Arboles, 'Jacarandá')) # 18
#print(arbolMasAlto_Especie(losAndes_Arboles, 'Jacarandá'))  # 21    Aca estoy agarrando otra lista, porque sino carece de sentido

#print(promedioArbol_Especie(general_paz_Arboles, 'Jacarandá' )) #10.2
#print(promedioArbol_Especie(centenario_Arboles, 'Jacarandá' )) #8.96


#5

#Igual al anterior

def obtener_inclinaciones(lista_arboles, especie):
    
    inclinacion_list = []
    
    for arbol in lista_arboles:
        
        alturaIndividual = arbol["inclinacio"]
        
        if arbol["nombre_com"] == especie:
            inclinacion_list.append(alturaIndividual)
            
    return inclinacion_list

#print(obtener_inclinaciones(general_paz_Arboles, 'Jacarandá'))

#6

#Para cada lista de arboles de un parque dar el que mas inclinacion tiene y de que especie es
#Es decir, encontrar el arbol mas inclinado y a dar la inclinacion de este.

# - Separar a la lista en especie y inclinacion
#      puedo crear una lista de cada especie con todas sus inclinaciones y tener un diccionario de cada especie con sus determinadas inclinaciones
#      o puedo crear una lista de tuplas inclinaciones y especie, asi encuentro el valor que mas inclinado este y dps para cuando haga el 7 ya tengo las cosas separadas 

def especimen_mas_inclinado(lista_arboles):
    
    masInclinado = []
    
    for arbol in lista_arboles:
        
        especie_individual = arbol["nombre_com"]
        inclinacion_individual = arbol["inclinacio"]
        masInclinado.append((especie_individual,inclinacion_individual))

    elMasInclinado = max(masInclinado, key = lambda x: x[1] )
    
    return elMasInclinado


#print(especimen_mas_inclinado(general_paz_Arboles))

#7

#Es tarde, no se me ocurre bien si hacerlo con un diccionario de especies y sus inclinaciones como clave, o si otra solucion es mas viable.

#def especie_promedio_mas_inclinada(lista_arboles):
    
    
