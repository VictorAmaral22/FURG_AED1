# Exrc 3
# A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:

# - Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

# π = 3.14159
# raio = float(input())
# area = π*(raio**2)

# print(f"A={area:.4f}")


# Exrc 4

# a = int(input(""))
# b = int(input(""))
# soma = a + b
# print(f"SOMA = {soma}")

# Exrc 5

# a = int(input(""))
# b = int(input(""))
# prod = a * b
# print(f"PROD = {prod}")

# Exrc 6

# a = (float(input(""))*3.5)/11
# b = (float(input(""))*7.5)/11

# media = a+b

# print(f"MEDIA = {media:.5f}")

# Exrc 7

# a = (float(input(""))*2)/10
# b = (float(input(""))*3)/10
# c = (float(input(""))*5)/10

# media = a+b+c

# print(f"MEDIA = {media:.1f}")

# Exrc 8

# a = int(input(""))
# b = int(input(""))
# c = int(input(""))
# d = int(input(""))

# diferenca = (a*b)-(c*d)

# print(f"DIFERENCA = {diferenca}")

# Exrc 9

# number = int(input())
# hours = int(input())
# value = float(input())

# print(f"NUMBER = {number}")
# print(f"SALARY = U$ {(hours*value):.2f}")

# Exrc 10

# name = input()
# salary = float(input())
# sales = float(input())

# extra = salary + (sales*0.15)

# print(f"TOTAL = R$ {extra:.2f}")

# Exrc 10

piece1 = input()
piece2 = input()

piece1 = piece1.split(" ")
piece2 = piece2.split(" ")

total = float(piece1[1])*float(piece1[2]) + float(piece2[1])*float(piece2[2])

print(f"VALOR A PAGAR: R$ {total:.2f}")