# idade = int(input("idade: "))
# if 18 <= idade >=67:
#     print("pode doar sangue")
# else: 
#     print("nao pode doar samge")

# x = int(input("x: "))
# y = int(input("y: "))
# print(f"x: {x}\ny: {y}")
# z = int(input("z: "))
# if x < z < y or y<z<x: 
#     print("z esta entre x e y")
# else:
#     print("z nao esta entre x e y")
def ex3():
    a = int(input())
    b = int(input())
    c = int(input())
    ordem = ""
    if a < b and a < c:
        ordem += str(a)
        ordem += " "
        if b < c:
            ordem += str(b)
            ordem += " "
            ordem += str(c)
            print(ordem)
        else: 
            ordem += str(c)
            ordem += " "
            ordem += str(b)
            print(ordem)
    else: 
        if b < a and b< c:
            ordem += str(b)
            ordem += " "
            print(ordem)
            if a < c:
                ordem += str(a)
                ordem += " "
                ordem += str(c)
                print(ordem)
            else: 
                ordem += str(c)
                ordem += " "
                ordem += str(a)
                print(ordem)
        else:
            if b < a:
                ordem += str(c)
                ordem += " "
                ordem += str(b)
                ordem += " "
                ordem += str(a)
                print(ordem)
            else:
                ordem += str(c)
                ordem += " "
                ordem += str(a)
                ordem += " "
                ordem += str(b)
                print(ordem, "=")
def ex5():
    x = int(input('x: '))
    n = int(input('n: '))
    pot = x
    while n > 1:
        x *= pot
        n -= 1
    print(x)
def ex8():
    num = 100
    while num <=450:
        div = num % 7
        if div == 0:
            print(num)
            num +=1
        else:
            num +=1
def ex9():
    n = int(input())
    soma = 0
    while n>0:
        num = int(input())
        soma += num
        n -= 1
    print("soma = ",soma)

def fatorial():
    n = int(input())
    a = 1
    b = n
    while a<b:
        n *= a
        a += 1
    print(n)

fatorial()