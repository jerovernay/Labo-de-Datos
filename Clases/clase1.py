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

#print(mezclar("Pepe", "Josefa"))


#4

#Termino pagando menos de lo que en realidad deberia de estar pagando

def pagoDavid(montoPrestado, pagoMensual):
    total = 0
    saldoRestante = montoPrestado
    interesMensual = ((1.05) ** (1/12)) - 1  
    
    while saldoRestante > 0:
        saldoRestante += (saldoRestante * interesMensual)
        pago = min(pagoMensual,saldoRestante)
        saldoRestante -= pago
        total += pago
        
    return round(total, 2)

#print(pagoDavid(500000, 2684.11))
        
def pagoDavid2(montoPrestado, pagoMensual, pagoAdelanto, cantMesesAdelanto):
    total = 0
    saldoRestante = montoPrestado
    interesMensual = ((1.05) ** (1/12)) - 1  
    meses = 0
    
    while saldoRestante > 0:
        saldoRestante += saldoRestante * interesMensual
        
        if meses < cantMesesAdelanto:
            pago = min(pagoMensual + pagoAdelanto, saldoRestante)
        elif meses >= cantMesesAdelanto:
            pago = min(pagoMensual, saldoRestante)
        
        meses += 1
        saldoRestante -= pago    
        total += pago
        
    return round(total, 2), meses 

#print(pagoDavid2(500000, 2684.11, 1000, 12))

def pagoDavid3(montoPrestado, pagoMensual, pagoAdelanto, comienzoMes, finalizaAdelantoMesMes ):
    total = 0
    saldoRestante = montoPrestado
    interesMensual = ((1.05) ** (1/12)) - 1  
    meses = 0
    
    while saldoRestante > 0:
        saldoRestante += saldoRestante * interesMensual
    
        if comienzoMes <= meses < finalizaAdelantoMesMes:
            pago = min(pagoMensual + pagoAdelanto, saldoRestante)
        else:
            pago = min(pagoMensual, saldoRestante)
    
        meses += 1
        saldoRestante -= pago    
        total += pago
        
    return round(total, 2), meses 

#print(pagoDavid3(500000, 2684.11, 1000, 60, 108))

#5

def geringoso(word):
    gerin = ""
    
    for letter in word:
        gerin += letter
        if letter in "AEIOUaeiou":
            gerin += "p" + letter
        
    return gerin

def traductor_geringoso(lista:list) -> dict:

    diccionario = {}
    
    for elem in lista:
        diccionario[elem] = geringoso(elem)
        
    return diccionario

print(traductor_geringoso(['banana', 'manzana', 'mandarina']))





