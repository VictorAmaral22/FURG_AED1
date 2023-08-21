# 11) Escreva um programa que mostre a tabuada (0 a 10) de um número fornecido pelo usuário

c = 1
n = int(input("Informe um número: "))

while c <= 10:
    print(f"{n} x {c} = {n*c}")
    c = c + 1