# 13) Escreva um programa que calcule e mostre a soma dos números de 1 a N. Não utilize
# as equações de progressão aritmética.

c = 1
num = int(input("Informe um número: "))
total = 0

while c <= num:
    total = total + c
    c = c + 1

print(total)