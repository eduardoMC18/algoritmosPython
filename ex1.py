# num = int(input("digite um numero:" ))
# tNum = num * 3
# dANum = (num + 1) * 2
# print( tNum - dANum )

# base = float(input("base: "))
# altura = float(input("altura: "))
# print("area: ", (base * altura)/2)

# salario_mensal = float(input("salario: "))
# percentual_de_reajuste = float(input("percentual: "))
# salario = (percentual_de_reajuste/100) * salario_mensal
# salario_atual = salario_mensal + salario 
# print(salario_atual)

# aresta = float(input("aresta do cubo: "))
# volume = aresta ** 3
# print(volume)

# distancia = float(input("distancia em km: "))
# gasto = float(input("gasto em litro: "))
# print(distancia/gasto,"km/L")

# comprimento = float(input("comprimento: "))
# largura = float(input("largura: "))
# preço_do_metro = float(input("preço do metro(R$/m^2): "))
# area = comprimento * largura
# print("custo total: ",area * preço_do_metro,"R$")

# peso = float(input("peso: "))
# altura = float(input("altura: "))
# imc = peso / (altura ** 2)
# print("IMC: ",imc)

# valor = float(input("valor do concurso: "))
# primeiro = (46/100) * valor
# segundo = (32/100) * valor 
# terceiro = (22/100) * valor 
# print(f"primeiro: {primeiro}R$ \n segundo: {segundo}R$ \n terceiro: {terceiro}R$")
valor_da_compra = float(input("valor da compra: "))
valor_pago = float(input("valor pago: "))
troco = valor_pago - valor_da_compra
def algBom(troco):
    print("troco: ", troco)
    print("EM: ")
    while troco >= 0:
        if troco >= 100:
            for i in range(int(troco/100)):
                troco = troco - 100
            print(f"R$ 100,00       {i + 1} cedulas")
        elif 100 > troco >= 50:
            for i in range(int(troco/50)):
                troco = troco - 50
            print(f"R$ 50,00       {i + 1} cedulas")
        elif 50 > troco >= 20:
            for i in range(int(troco/20)):
                troco = troco - 20
            print(f"R$ 20,00       {i + 1} cedulas")
        elif 20 > troco >= 10:
            for i in range(int(troco/10)):
                troco = troco - 10
            print(f"R$ 10,00       {i + 1} cedulas")
        elif 10 > troco >= 5:
            for i in range(int(troco/5)):
                troco = troco - 5
            print(f"R$ 5,00       {i + 1} cedulas")
        elif 5 > troco >= 1:
            for i in range(int(troco/1)):
                troco = troco - 1
            print(f"R$ 1,00       {i + 1} cedulas")

def algRuim(troco):
    notasCem = troco // 100
    trocoAt = troco - (100 * notasCem)
    notasCinquenta = trocoAt // 50
    trocoAt = trocoAt - (50*notasCinquenta)
    notasVinte = trocoAt // 20
    trocoAt = trocoAt - (20*notasVinte)
    notasDez = trocoAt // 10
    trocoAt = trocoAt - (10*notasDez)
    notasCinco = trocoAt // 5
    trocoAt = trocoAt - (5*notasCinco)
    notasUm = trocoAt
    print(f"troco EM\nR$ 100,00       {notasCem} cedulas\nR$ 50,00       {notasCinquenta} cedulas\nR$ 20,00       {notasVinte} cedulas\nR$ 10,00       {notasDez} cedulas\nR$ 5,00       {notasCinco} cedulas\nR$ 1,00       {notasUm} cedulas")
    
algRuim(troco)
