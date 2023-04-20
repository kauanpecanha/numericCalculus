# -*- coding: utf-8 -*-
"""CNBissectionMethod.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OwWGqBlAx_9oVxoS2jPGsc8WHaOTNE5x
"""

# Commented out IPython magic to ensure Python compatibility.

# método da bisseção

# importação das bibliotecas

# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

tol = 0
x = 0
iteration = 0

def setXn(k, l):
    return ((k+l)/(2))

def f(x):
    return # a função deve ser inserida aqui, e na variável yf

def setTol(i, j):
    return (abs(j - i))

a = float(input("Entre com o primeiro número do intervalo: "))
b = float(input("Entre com o segundo número do intervalo: "))
epsilon = float(input('Entre com a tolerância desejada: '))


xf = np.linspace(a-1, b+1, 100)
# yf = # insira a função aqui
a_zero = a
b_zero = b

tol = setTol(a, b)

while(tol>epsilon):
    x = setXn(a, b)

    f_a = f(a)
    f_B = f(b)
    f_x = f(x)

    if((f_a)*(f_x)<0):
        b = x
    else:
        a = x
    
    tol = setTol(a, b)

    print(f'ITERATION {iteration} - Range of possible solutions: [{a:.4f}, {b:.4f}], near {x:.4f}')

    iteration+=1

# xf = np.linspace(a-1, b+1, 100)
# yf = xf**3 - 9*xf + 3

plt.grid()
plt.scatter(a, f(a), c='blue')
plt.scatter(b, f(b), c='blue')
plt.scatter(a_zero, f(a_zero), c='red')
plt.scatter(b_zero, f(b_zero), c='red')
plt.plot(xf, yf, c='purple')

print('Aproximação final:')