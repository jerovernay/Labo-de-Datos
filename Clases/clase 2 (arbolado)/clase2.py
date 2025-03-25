import csv
import pandas as pd

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
losAndes_Arboles = leer_parque(nombre_archivo, 'ANDES, LOS') 

#print(contar_ejemplares(losAndes_Arboles)) #Funciona


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
#print(arbolMasAlto_Especie(losAndes_Arboles, 'Jacarandá'))  # 25

#print(promedioArbol_Especie(general_paz_Arboles, 'Jacarandá' )) #10.2
#print(promedioArbol_Especie(centenario_Arboles, 'Jacarandá' )) #8.96
#print(promedioArbol_Especie(losAndes_Arboles, 'Jacarandá')) #10.54

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

def especie_promedio_mas_inclinada(lista_arboles):
    
    dict_Inclinaciones_Especie = {}
    
    for arbol in lista_arboles:
        
        especie = arbol["nombre_com"]
        inclinacion = arbol["inclinacio"]
        
        if especie in dict_Inclinaciones_Especie:    
            dict_Inclinaciones_Especie[especie].append(inclinacion)
        else:
           dict_Inclinaciones_Especie[especie] = [inclinacion]
    
    dict_Inclinaciones_Especie_Promedio = {}
    
    for especie, inclinaciones in dict_Inclinaciones_Especie.items():
        dict_Inclinaciones_Especie_Promedio[especie] = round(sum(inclinaciones)/ len(inclinaciones), 3)
        
    clave_maxValue = max(dict_Inclinaciones_Especie_Promedio, key = dict_Inclinaciones_Especie_Promedio.get())
    maxValue = dict_Inclinaciones_Especie_Promedio[clave_maxValue]
    
    return maxValue      
           
#print(especie_promedio_mas_inclinada(general_paz_Arboles))    # No se donde me equivoco!!!   

#8


archivo_veredas = 'arbolado-vereda.csv'

df = pd.read_csv(archivo_veredas)

secciones_interes = ['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']
df_reducido =df[secciones_interes]

df_veredas = df_reducido[(df_reducido['nombre_cientifico'] == 'Tilia x moltkei' ) | 
                             (df_reducido['nombre_cientifico'] == 'Jacaranda mimosifolia')|
                              (df_reducido['nombre_cientifico'] == 'Tipuana tipu' )]
                              
# print(df_veredas.head())

dfP = pd.read_csv(nombre_archivo)   

secciones_interes2 = ['nombre_cie', 'diametro', 'altura_tot']
dfP_reducido = dfP[secciones_interes2]

especies_seleccionadas = ['Tilia viridis subsp. x moltkei', 'Jacaranda mimosifolia', 'Tipuana Tipu']
df_parques = dfP_reducido[dfP_reducido['nombre_cie'].isin(especies_seleccionadas)]

# print(df_parques.head())

especies_seleccionadas_vereda = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'].isin(especies_seleccionadas_vereda)].copy()
df_tipas_parques = df_parques[df_parques['nombre_cie'].isin(especies_seleccionadas)].copy()

df_tipas_parques.rename(columns = { 'nombre_cie' : 'nombre_cientifico',
                                   'altura_tot' : 'altura_arbol'}, inplace = True)

df_tipas_veredas.rename(columns = {'diametro_altura_pecho' : 'diametro'}, inplace = True)

mismo_nombre_especie = {'Tilia viridis subsp. x moltkei' :'Tilia x moltkei' ,
                        'Tipuana Tipu' : 'Tipuana tipu' }

df_tipas_parques['nombre_cientifico'] = df_tipas_parques['nombre_cientifico'].replace(mismo_nombre_especie)

#print(df_tipas_parques.head())
#print(df_tipas_veredas.head())


#9

df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'

#print(df_tipas_parques.head())
#print(df_tipas_veredas.head())

#10

df_concat = pd.concat([df_tipas_parques, df_tipas_veredas], ignore_index= True)

#11

print(df_concat.sample(40))


# COMENTARIOS SOBRE LA PRACTICA Y CONSULTAS

# COMETO UN ERROR EN EL 7, CONSULTAR

# DESPUES, SOBRE EL ANALISIS DEL ULTIMO. ES UN POCO RARO PODER COMPARAR CON 3 TIPOS DE ARBOL DE UNA MANERA SIMPLE.
# SERIA MAS FACIL TRABAJAR SOBRE UN ARBOL SOLO Y CON ESO BASTARIA PARA COMPARAR. 

# CONSULTAR SI ES POSIBLE PODER ELEGIR EJEMPLARES UNICOS DE UNO Y EJEMPLARES UNICOS DEL OTRO, DENTRO DE LA SOLUCION CONCATENADA.
# DE SER ASI ES MAS FACIL ANALIZAR LOS DATOS. SINO ES PREFERIBLE AGARRAR UNA CANTIDAD FINITA DE SAMPLES Y DE AHI COMPARAR, PERO NO VEO MUY NECESARIO HACERLO EN UNA LISTA CONCATENADA, AL MENOS NO CON 3 TIPOS DE ARBOL DISTINTOS.


