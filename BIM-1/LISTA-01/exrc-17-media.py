# 17) Escreva um programa que leia diversos números até que o usuário digite zero. Em
# seguida escreva a média dos números digitados.

c = 1
num = float(input("Informe um número: "))
media = 0
soma = num

while num != 0:
    num = float(input("Informe um número: "))
    soma = soma + num
    
    if num != 0:
        c = c + 1

media = soma / c

print(media)