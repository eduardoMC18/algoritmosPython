# Peça o salário bruto de um cliente e o valor da prestação de um
# empréstimo. Se a prestação for maior que 30% do salário, o
# empréstimo é negado. Caso contrário, verifique o tempo de serviço:
# se for maior que 2 anos, o empréstimo é "Aprovado com Bônus", se
# não, apenas "Aprovado".
def ex8(): 
    salario = float(input('salario bruto: '))
    valorPrestacao = float(input('prestacao: '))

    if valorPrestacao >= 0.3*salario:
        print('emprestimo negado')
    else: 
        tempoDeServico = int(input('tempo de servico(em anos): '))
        if tempoDeServico >= 2:
            print('emprestimo aprovado com bonus')
        else:
            print('aprovado')

#      Leia o salário de um funcionário e determine o seu novo salário
# considerando que o aumento segue as regras abaixo.
# • Até R$ 1.500: aumento de 15%.
# • De R$ 1.501 a R$ 3.000: aumento de 10%.
# • Acima de R$ 3.000: aumento de 5%
def ex9():
    salario = float(input('salario: '))
    if salario <= 1500:
        novoSalario = salario * 1.15
    elif 1501 < salario < 3000:
        novoSalario = salario * 1.10
    else:
        novoSalario = salario * 1.05
    print(f'novo salario:  {novoSalario:0.2f}')

# Leia dois valores reais (x,y) representando as coordenadas
# de um ponto em um plano. Determine em qual quadrante o
# ponto se encontra (Q1, Q2, Q3 ou Q4) ou se está sobre um
# dos eixos ou na origem (0,0)

def ex10(): 
    x = int(input('x: '))
    y = int(input('y: '))
    if x > 0 and y>0:
        quadrante = 'Q1'
    elif x < 0 and y>0: 
        quadrante = 'Q2'
    elif x < 0 and y<0:
        quadrante = 'Q3'
    else: 
        quadrante = 'Q4'
    print(quadrante)

# Construa um programa que leia os três lados de um triângulo.
# Primeiro, verifique se eles formam um triângulo (cada lado deve ser
# menor que a soma dos outros dois). Se sim, classifique-o em:
# Equilátero (3 lados iguais), Isósceles (2 iguais) ou Escaleno (todos
# diferentes). Senão informe que os lados não representam um triângulo

def ex12(): 
    ladoUm = int(input('lado 1: '))
    ladoDois = int(input('lado 2: '))
    ladoTres = int(input('lado 3: '))
    if ladoUm < (ladoDois + ladoTres) and ladoDois < (ladoUm + ladoTres) and ladoTres < (ladoDois + ladoUm):
        if ladoUm == ladoDois == ladoTres:
            print('triangulo equilatero')
        elif ladoUm == ladoDois or ladoUm == ladoTres or ladoDois == ladoTres:
            print('triangulo isoceles')
        else: 
            print('triangulo escaleno')
    else:
        print('nao é um triangulo')

# exercicio 14 desafio
def ex14(): 
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    if (a * e) - (b * d) == 0: 
        print('equacao impossivel')
    else: 
        print(f"{a}x + {b}y = {c}\n{d}x + {e}y = {f}")
        x = ((c * e) - (b * f)) / ((a * e) - (b * d))
        y = ((a * f) - (c * d)) / ((a * e) - (b * d))
        print(f"x = {x:.2f}\ny = {y:.2f}")

ex14()