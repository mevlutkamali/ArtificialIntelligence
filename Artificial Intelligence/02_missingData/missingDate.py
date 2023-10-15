# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('eksikveriler.csv')
print(data)

# Burada bulunan eksik verilerin tüm sütünun ortalamalarını alarak elde edilebilir .

from sklearn.impute import  SimpleImputer

# SimpleImputer, scikit-learn kütüphanesinde bulunan bir sınıftır ve eksik verileri doldurmak için kullanılır. Veri analizi ve makine öğrenme projelerinde sıkça kullanılır çünkü gerçek dünya verileri genellikle eksik veya bozuk verilere sahiptir. SimpleImputer, bu eksik değerleri belirli bir stratejiye göre doldurmanıza yardımcı olur.

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

age = data.iloc[:, 1:4].values
print(age)

imputer = imputer.fit(age[:, 1:4])
age[:, 1:4] = imputer.transform(age[:, 1:4])
print(age)