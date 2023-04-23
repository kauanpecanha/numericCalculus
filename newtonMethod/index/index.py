# método de newton

# importação das bibliotecas

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos

def f(x):
    return (x**3 - 2*x**2 - 5)# define the function right here

def dF(x):
    return (3*x**2 - 4*x)# define the derivated function right here

def defineXn(x):
    return (x - ((f(x))/(dF(x))))

a = float(input("Entre com o primeiro número do intervalo: "))
b = float(input("Entre com o segundo número do intervalo: "))
fixedPoint = float(input("Entre com o ponto fixo: "))
epsilon = float(input('Entre com a tolerância desejada: '))
maximumIteration = float(input("Entre com o número máximo de iterações: ")) # definição do número máximo de iterações

iteration = 0 # variável para controle do número de iterações
xf = np.linspace(a-1, b+1, 1000)

print(f'\nITERAÇÃO: {iteration} - \nPonto fixo: {fixedPoint},\n f({fixedPoint}) = {f(fixedPoint)},\n f*({fixedPoint}) = {dF(fixedPoint)}\n')
x = defineXn(fixedPoint)

iteration+=1

while(True):
    if(iteration<maximumIteration):
        if(abs(f(x)) >= epsilon):
            
            print(f'\nITERAÇÃO: {iteration} - \nCurrent x: {x:.4f},\n f({x:.4f}) = {f(x):.4f},\n f*({x:.4f}) = {dF(x):.4f}\n')
            x = defineXn(x)
            print(f'\nITERAÇÃO: {iteration} - \nx foi definido como {x:.4f}\n')

            iteration = iteration + 1
        
        else:
            print(f'\nITERAÇÃO: {iteration} - \n|f({x})| = {abs(f(x)):.4f} < {epsilon}. Ciclos encerrados!')
            print(f'\nITERAÇÃO: {iteration} - \nRaiz aproximada: {x:.4f}')
            break
    else:
        print(f'\nITERAÇÃO: {iteration} - \nO número máximo de iterações foi atingido!')
        print(f'\nITERAÇÃO: {iteration} - \nRaiz aproximada: {x}')
        break

plt.grid()
plt.scatter(a, f(a), c='red')
plt.scatter(b, f(b), c='red')
plt.scatter(x, f(x), c='blue')
plt.plot(xf, f(xf), c='purple')