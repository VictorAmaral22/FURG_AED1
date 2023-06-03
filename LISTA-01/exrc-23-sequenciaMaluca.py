# 23) Considere uma sequência de números que atende a todos critérios abaixo: 

# a - Possui sempre 2 dígitos, nem mais, nem menos. 
# b - A representação do número possui pelo menos um dígito 1 ou um dígito 2. 
# c - O número é múltiplo de 3. 

# Faça um programa que implemente e mostre essa sequência. obs: tem que usar repetição para mostrar a sequência. Não pode mostrar os números “na mão”.

c = 10

while c < 100:
    if c%10 == 1 or c%10 == 2 or c//10 == 1 or c//10 == 2:
        if c%3 == 0:
            print(c)

    c = c + 1