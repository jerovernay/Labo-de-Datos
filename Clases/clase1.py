# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

#1
def pertenece(lista , elem):
    if elem in lista:
        return True
    else:
        return False
    
#print(pertenece([1,2,3,4,5], 6))

#2 
def mas_larga(list1, list2):
    if len(list1) >= len(list2):
        return list1
    else:
        return list2
    
#print(mas_larga([1,2,4], [3,4,5,6,6]))
#3
    
    
def mezclar(cadena1, cadena2):
    res = ""
    i = 0
    
    while i < len(cadena1) or i < len(cadena2):
        
        if i < len(cadena1):
            res += cadena1[i]
        if i < len(cadena2):
        
            res +=cadena2[i]
            
        i += 1
            
    return res

print(mezclar("Pepe", "Josefa"))


#4

# def pagoDavid(montoPrestado, cantAños, pagoMensual):
#     total = montoPrestado
#     saldoRestante = montoPrestado
#     cantMeses = cantAños * 12
#     interesMensual = ((1.05) ** (1/12)) - 1  
    
#     for i in range(0,cantMeses):
#         saldoRestante -= (saldoRestante - pagoMensual) * interesMensual
            
        
    
#5

def traductor_geringoso(lista) -> dict:
