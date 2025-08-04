#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 22:04:07 2023

@author: mcerdeiro
"""
#%% modulos

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import tree
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import MinMaxScaler

#%%######################

        ####            Cargo dataset

#########################
#%%        


# iris = load_iris(as_frame = True)

# data = iris.frame
# X = iris.data
# Y = iris.target

# iris.target_names
# diccionario = dict(zip( [0,1,2], iris.target_names))
#%%######################

        ####            Un primer modelo

#########################
#%%  
# model = KNeighborsClassifier(n_neighbors = 5) # modelo en abstracto
# model.fit(X, Y) # entreno el modelo con los datos X e Y
# Y_pred = model.predict(X) # me fijo qué clases les asigna el modelo a mis datos
# metrics.accuracy_score(Y, Y_pred)
# metrics.confusion_matrix(Y, Y_pred)

#%%        
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3) # 70% para train y 30% para test

# model = KNeighborsClassifier(n_neighbors = 5) # modelo en abstracto
# model.fit(X_train, Y_train) # entreno el modelo con los datos X_train e Y_train
# Y_pred = model.predict(X_test) # me fijo qué clases les asigna el modelo a mis datos X_test
# print("Exactitud del modelo:", metrics.accuracy_score(Y_test, Y_pred))
# metrics.confusion_matrix(Y_test, Y_pred)
# print(metrics.confusion_matrix(Y_test, Y_pred))
#%%

# ¿QUÉ PASA SI REPETIMOS CON OTRO SPLIT?

#%%

# Nrep = 5
# valores_n = range(1, 20)

# resultados_test = np.zeros((Nrep, len(valores_n)))
# resultados_train = np.zeros((Nrep, len(valores_n)))


# for i in range(Nrep):
#     X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3)
#     for k in valores_n:
#         model = KNeighborsClassifier(n_neighbors = k)
#         model.fit(X_train, Y_train) 
#         Y_pred = model.predict(X_test)
#         Y_pred_train = model.predict(X_train)
#         acc_test = metrics.accuracy_score(Y_test, Y_pred)
#         acc_train = metrics.accuracy_score(Y_train, Y_pred_train)
#         resultados_test[i, k-1] = acc_test
#         resultados_train[i, k-1] = acc_train

#%%

# promedios_train = np.mean(resultados_train, axis = 0) 
# promedios_test = np.mean(resultados_test, axis = 0) 
# #%%

# plt.plot(valores_n, promedios_train, label = 'Train')
# plt.plot(valores_n, promedios_test, label = 'Test')
# plt.legend()
# plt.title('Exactitud del modelo de knn')
# plt.xlabel('Cantidad de vecinos')
# plt.ylabel('Exactitud (accuracy)')
#%%

#%%

# ¿QUÉ PASA SI REPETIMOS MÁS VECES?

#%%


arboles = pd.read_csv("arboles.csv")

#print(arboles.columns)

X = arboles[["altura_tot", "inclinacio", "diametro"]] #"nombre_com"
Y = arboles["nombre_com"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3)

scaler = MinMaxScaler()
X_train_norm = scaler.fit_transform(X_train)
X_test_norm = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors = 5) # modelo en abstracto
model.fit(X_train_norm, Y_train) # entreno el modelo con los datos X_train e Y_train
Y_pred = model.predict(X_test_norm) # me fijo qué clases les asigna el modelo a mis datos X_test
print("Exactitud del modelo:", metrics.accuracy_score(Y_test, Y_pred))
metrics.confusion_matrix(Y_test, Y_pred)
print(metrics.confusion_matrix(Y_test, Y_pred))



Nrep = 5
valores_n = range(1, 20)
resultados_test = np.zeros((Nrep, len(valores_n)))
resultados_train = np.zeros((Nrep, len(valores_n)))

for i in range(Nrep):
    # Dividir datos (con random_state para reproducibilidad)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=i)
    
    # Normalizar los datos (importante para KNN)
    # scaler = MinMaxScaler()
    # X_train_norm = scaler.fit_transform(X_train)
    # X_test_norm = scaler.transform(X_test)
    
    for j, k in enumerate(valores_n):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, Y_train)
        
        # Predecir en test y train
        Y_pred_test = model.predict(X_test)
        Y_pred_train = model.predict(X_train_norm)
        
        # Calcular exactitudes
        resultados_test[i, j] = metrics.accuracy_score(Y_test, Y_pred_test)
        resultados_train[i, j] = metrics.accuracy_score(Y_train, Y_pred_train)

#%%

promedios_train = np.mean(resultados_train, axis = 0) 
promedios_test = np.mean(resultados_test, axis = 0) 
#%%

plt.plot(valores_n, promedios_train, label = 'Train')
plt.plot(valores_n, promedios_test, label = 'Test')
plt.legend()
plt.title('Exactitud del modelo de knn')
plt.xlabel('Cantidad de vecinos')
plt.ylabel('Exactitud (accuracy)')
plt.show()
        
        
        
        
        
        
        
        
        
        
        