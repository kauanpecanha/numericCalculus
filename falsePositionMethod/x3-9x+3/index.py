
# método da bisseção(ou valor intermediário?)

a = float(input("Entre com o primeiro número do intervalo: "))
b = float(input("Entre com o segundo número do intervalo: "))
epsilon = float(input('Entre com a tolerância desejada: '))

tol = 0
x = 0
iteration = 0

def getFunc(x):
    return ((x**3) - (9 * x) + (3))

def setXn(k, l):
    return ( # esta sintaxe visa melhorar a visualização dos parâmetros - este parênteses determina o resultado como um todo
            
            ((k * (getFunc(l))) - (l * (getFunc(k)))) # numerador da fração
            /
            ((getFunc(l) - getFunc(k))) # denominador da fração

        )

while(getFunc(x) >= epsilon):
    
    x = setXn(a, b)

    if(getFunc(a) * getFunc(x) < 0):
        b = x
    else:
        a = x
    
    iteration += 1

print(f'A raiz aproximada dessa função é {x}, se encontra no intervalo [{a}, {b}], e foi encontrado após {iteration} iterações.')