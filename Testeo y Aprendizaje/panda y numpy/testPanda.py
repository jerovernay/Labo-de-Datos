# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 17:55:01 2025

@author: jeron
"""

import pandas as pd
import numpy as np

d = {'nombre':['Antonio', 'Brenda', 'Camilo', 'David'], 'apellido': ['Restrepo', 'Saenz',
'Torres', 'Urondo'], 'lu': ['78/23', '449/22', '111/24', '1/21']}

df = pd.DataFrame(data= d) # creamos un dataframe a partir de un diccionario
df.set_index('lu', inplace = True) # seteamos una columna como indice

M = np.array([[11, 1, -5, 3],[10, 5, 6, 7],[3, 8, 10, -1]])
df2 = pd.DataFrame(data = d) # creamos un df a partir de un array
df2 = pd.DataFrame(M, columns = ['a', 'b', 'c', 'd'], index = ['v1', 'v2', 'v3'])


