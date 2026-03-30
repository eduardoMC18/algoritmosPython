def ex1(num):
    print(num - 1, num + 1)

def lerNum():
    num = int(input("num: "))
    return num

def ex2():
    num1 = lerNum()
    num2 = lerNum()
    num3 = lerNum()
    print(num1 + num2 + num3)

# Faça um programa com uma função chamada somaImposto. A
# função possui dois parâmetros formais: taxaImposto, que é a quantia
# de imposto sobre vendas expressa em porcentagem e custo, que é o
# custo de um item antes do imposto. A função “altera” o valor de custo
# para incluir o imposto sobre vendas

def somaImposto(taxaImposto, custo):
    custo = custo * ((taxaImposto/100) + 1)
    print(custo)

def ex4(a, b):
    if b > a:
        for i in range(b+1):
            if i >=a and i%2 == 0:
                print(i)
    else:
        for i in range(a+1):
            if i >=b and i%2 == 0:
                print(i)

def ex6(n):
    fatorial = 1
    for i in range(n):
        fatorial = (i + 1) * fatorial

    print(fatorial)

def somarTudo():
    n1 = lerNum()
    n2 = lerNum()
    rep = n2 - n1
    result = 0
    for i in range(rep+1):
        result += n1 + i
    print(result)

# somarTudo()

def numPerfeito(num):
    soma = 0
    for i in range(num):
        if num%(i+1) == 0 and (i+1) != num:
            soma += (i+1)
    if soma == num:
        print("NUMERO PERFEITO")
    else:
        print("NUMERO NAO PERFEITO")
    
def somarDigitos(num):
    soma = 0
    tamanhoNum = 2
    for i in range(tamanhoNum):
        a = num // 10**(i)
        print(i)
        soma += a
    print(soma)

somarDigitos(12)