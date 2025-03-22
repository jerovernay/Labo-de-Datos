# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 16:38:46 2025

@author: jeron
"""

nombre_archivo = 'cronograma_sugerido.csv'

#materias = []

with open(nombre_archivo, 'r', encoding= 'utf-8') as file:
    for line in file:
        datos_linea = line.split(',')
        
        #materias.append(datos_linea[1])
        
#print(materias)
#print(datos_linea[1])
        
        