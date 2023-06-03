# 12) Escreva um programa que mostre a seguinte sequência de números para um valor N informado pelo usuário:

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# …
# N N N N N N N …

num = int(input("Informe um número: "))
c = 1

while c <= num:
    c2 = 0
    while c2 < c:
        print(c, end="")
        c2 = c2 + 1
    print("")

    c = c + 1