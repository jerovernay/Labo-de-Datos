# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 16:24:49 2025

@author: jeron
"""

nombre_archivo = 'datame.txt'
with open(nombre_archivo, 'r', encoding='utf-8') as f:
    data = f.read()

data_nuevo = '2024 seguimos con Datame\n\n' + data
data_nuevo = data_nuevo + 'Direccion de Carrera LCD'

datame = open('datame_2024.txt', 'w')
datame.write(data_nuevo)
datame.close()


with open('datame_2024.txt', 'r') as file:
    datameTXT = file.read()
    
print(datameTXT)