# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 14:59:07 2023

@author: kamal
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('eksikveriler.csv')
print(data)

countrys = data.iloc[:, 0:1].values
print(countrys)

from sklearn import preprocessing

# Verileri sayısal değerlere dönüştürmek için preprocessing.LabelEncoder sınıfını kullanıyoruz.
le = preprocessing.LabelEncoder()

countrys[:, 0] = le.fit_transform(data.iloc[:, 0])

print(countrys)

# One-hot encoding, kategorik verileri sayısal matrislere dönüştürmek için kullanılır.
ohe = preprocessing.OneHotEncoder()
countrys = ohe.fit_transform(countrys).toarray()
print(countrys)
