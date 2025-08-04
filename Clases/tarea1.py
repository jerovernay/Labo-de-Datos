#1

empleado_01 = [[20222333, 45, 2, 20000],
               [33456234, 40, 0, 25000],
               [45432345, 41, 1, 10000]]

#2

empleado_02 = [[20222333, 45, 2, 20000],
               [33456234, 40, 0, 25000],
               [45432345, 41, 1, 10000],
               [43967304, 37, 0, 12000],
               [42236276, 36, 0, 18000]]

def superanSalarioActividad_01 (empleados, umbral):
    listaFinal = []
    
    for empleado in empleados:
        if empleado[3] > umbral:
            listaFinal.append(empleado)
            
    return listaFinal

#print(superanSalarioActividad_01(empleado_02, 15000)) #sigue funcionando bien

#3

empleado_03 = [[20222333, 20000, 45, 2],
               [33456234, 25000, 40, 0],
               [45432345, 10000, 41, 1],
               [43967304, 12000, 37, 0],
               [42236276, 18000, 36, 0]]
 
#Tengo que cambiar lo de empleado nomas, muy sencillo

def superanSalarioActividad_03 (empleados, umbral):
    listaFinal = []
    
    for empleado in empleados:
        if empleado[1] > umbral:
            listaFinal.append(empleado)
            
    return listaFinal

#print(superanSalarioActividad_03(empleado_03, 15000))


#4

empleado_04 = [[20222333, 33456234, 45432345, 43967304, 42236276],
               [20000, 25000, 10000, 12000, 18000],
               [45, 40, 41, 37, 36],
               [2, 0, 1, 0, 0]]

def superanSalarioActividad_04 (empleados, umbral):
    listaFinal = []
    
    for i in range(len(empleados[0])):
        if empleados[1][i] > umbral:
            listaFinal.append([empleados[0][i], empleados[1][i], empleados[2][i], empleados[3][i]])
            
    return listaFinal

#print(superanSalarioActividad_04(empleado_04, 15000))


#5

# 1. no cambio mucho, sinceramente fue variar el parametro de busqueda en el bucle for en ambos casos

# 2. Cuando se realizo el cambio lo que llevo un poco mas de tiempo fue ver que habia que iterar por sobre columnas propiamente
#    en vez de por las filas.
   
# 3. no entendi la pregunta, por como estaba elaborada.



