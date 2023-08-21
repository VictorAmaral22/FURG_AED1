# 1) (5 Pontos) Considere um programa em Python que simula um jogo de cartas com um baralho completo. 
# O baralho é inicializado com 52 cartas, divididas em 4 naipes
# (Paus, Ouros, Copas e Espadas) e 13 valores (de 2 a 10, Valete, Dama, Rei e Ás). 
# O programa deve utilizar listas para armazenar o baralho e sortear duas cartas para
# cada um de 6 jogadores. Mostre na tela cada uma das cartas sorteadas para cada
# jogador. Você não deve permitir que uma carta seja sorteada mais de uma vez.

import random

naipes = ["Paus", "Ouros", "Copas", "Espadas"]
numeros = [2,3,4,5,6,7,8,9,10, "Valete", "Dama", "Rei", "Ás"]
hands = []

c = 0
while c < 6:
    handResult = []
    
    c2 = 0
    while c2 < 2:
        naipeid = random.randint(0, len(naipes)-1)
        numeroid = random.randint(0, len(numeros)-1)

        if len(hands) > 0:
            c3 = 0
            while c3 < len(hands):
                for card in hands[c3]:
                    if card[0] ==  naipeid and card[1] == numeroid:
                        # print("Tem igual "+str(numeros[card[1]])+" de "+naipes[card[0]])
                        naipeid = random.randint(0, len(naipes)-1)
                        numeroid = random.randint(0, len(numeros)-1)
                        c3 = 0                    

                c3 = c3 + 1

        handResult.append([naipeid, numeroid])
        c2 = c2 + 1
    
    print("Jogador "+str(c+1)+", a sua mão é : ")
    for card in handResult:
        print("- "+str(numeros[card[1]])+" de "+naipes[card[0]])
    print("")

    hands.append(handResult)
    c = c + 1