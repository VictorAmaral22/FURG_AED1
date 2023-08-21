# 14) Escreva um programa que receba um número inteiro positivo do usuário e verifique
# se ele é primo.

c = 2
primo = int(input("Informe um número: "))
divisions = 0

while c <= primo:
    if divisions > 1:
        c = primo+1
    else:
        if primo % c == 0:
            divisions = divisions + 1

        c = c + 1

if divisions == 1:
    print("É primo")
else:
    print("Não é primo!")