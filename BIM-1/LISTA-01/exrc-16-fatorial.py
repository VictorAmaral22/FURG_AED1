# 16) Escreva um programa que calcule o fatorial de um número fornecido pelo usuário. O
# fatorial de um número n é o produto de todos os números inteiros de 1 a n.

c = 1
num = int(input("Informe um número: "))
fator = 1

while c <= num:
    fator = fator * c
    c = c + 1

print(fator)