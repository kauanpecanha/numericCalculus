
# método da bisseção(ou valor intermediário?)

a = float(input("Entre com o primeiro número do intervalo: "))
b = float(input("Entre com o segundo número do intervalo: "))
epsilon = float(input('Entre com a tolerância desejada: '))
tol = 0
x = 0
iteration = 0

def setXn(k, l):
    return ((k+l)/(2))

def setFunc(x):
    return ((x)**3) - 9*(x) + 3

def setTol(i, j):
    return (abs(j - i))

tol = setTol(a, b)

while(tol>epsilon):
    x = setXn(a, b)

    f_a = setFunc(a)
    f_B = setFunc(b)
    f_x = setFunc(x)

    if((f_a)*(f_x)<0):
        b = x
    else:
        a = x
    
    tol = setTol(a, b)

    iteration+=1

print(f'Total of iterations: {iteration}')