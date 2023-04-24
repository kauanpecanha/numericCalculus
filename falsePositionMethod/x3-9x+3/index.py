
# método da bisseção

a = float(input("Entre com o primeiro número do intervalo: "))
b = float(input("Entre com o segundo número do intervalo: "))
epsilon = float(input('Entre com a tolerância desejada: '))

x = 0
iteration = 0

def f(x):
    return ((x**3) - (9 * x) + (3))

def setXn(k, l):
    return ( # esta sintaxe visa melhorar a visualização dos parâmetros - este parênteses determina o resultado como um todo
            
            ((k * (f(l))) - (l * (f(k)))) # numerador da fração
            /
            ((f(l) - f(k))) # denominador da fração

        )

plt.scatter(a, f(a), c='red') # destaca o ponto no gráfico que representa a raiz
plt.scatter(b, f(b), c='red') # destaca o ponto no gráfico que representa a raiz

while(True):
    
    x = setXn(a, b) # 0.3386

    print(f'k = {iteration} ; a = {a:.4f} ; b = {b:.4f} ; f({a:.4f}) = {f(a):.4f} ; f({b:.4f}) = {f(b):.4f} ; xk = {x:.4f} ; |f({x:.4f})| = { (abs(f(x))) }')
    
    if( abs( f(x) ) < epsilon): # se 0.008 < 0.065

        print(f'Na iteração {iteration}, foi atingido o valor aproximado da raiz: {x}')

        break

    if( f(a) * f(x) < 0):
        b = x # b = 0.375
    else:
        a = x

    
    iteration+=1

plt.grid()
plt.scatter(x, f(x), c='blue') # destaca o ponto no gráfico que representa a raiz
plt.plot( np.linspace(a-1, b+1, 1000), f(np.linspace(a-1, b+1, 1000)), c='purple')