
# método de Newton-Raphson

a = float(input("Entre com o primeiro número do intervalo: "))
b = float(input("Entre com o segundo número do intervalo: "))
fixedPoint = float(input("Entre com o ponto fixo: "))
epsilon = float(input('Entre com a tolerância desejada: '))
maximumIteration = float(input("Entre com o número máximo de iterações: ")) # definição do número máximo de iterações


x = 0
iteration = 0 # variável para controle do número de iterações

# criação das variáveis (acima)

def getFunc(x):
    return ((x**3) - (2*x**2) - (5))

def getDerivateFunc(x):
    return ((3*x**2) - (4*x))

def defineXn(x):
    return (x - ((getFunc(x))/(getDerivateFunc(x))))

# the functions are working well!

while(
        ((abs(getFunc(fixedPoint))) <= epsilon) # if the modulus os f(x) is less than the epsilon, then, the iteration is going to come to an end
            or
        (iteration<maximumIteration) # if the iteration reachs the maximum number set of iterations, then, the iteration is going to come to and end
    ): 

    if(iteration == 0):
        x = defineXn(fixedPoint)
    else:
        x = defineXn(x)
    
    iteration+=1

print(f'O valor final da raiz é {x}, após {iteration} iterações, com precisão de {epsilon}')