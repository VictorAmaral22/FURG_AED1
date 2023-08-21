# 19) Escreva um programa de adivinhação de número. O programa deve conter um
# número secreto entre 1 e 1.000.000. O usuário deve chutar um número e o
# programa deve dizer se o número chutado é maior ou menor que o número secreto.
# O usuário deve tentar até acertar o número secreto. O código abaixo mostrar como
# sortear um número aleatório entre 0 e 10 em python:

import random

randomNum = random.randint(0, 1000000)
# print(randomNum)

trial = int(input("Dê um chute: "))

while trial != randomNum:
    if trial > randomNum:
        print(f"O número aleatório é menor que {trial}...")
    if trial < randomNum:
        print(f"O número aleatório é maior que {trial}...")
    
    trial = int(input("Dê um chute: "))

if trial == randomNum:
    print("Acerto miseravi")
