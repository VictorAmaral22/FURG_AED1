# Exercício notas
# Leia 4 notas
# Lei a frequência em %
#  media >= 7 - passa por média
# 3 < media < 7 - exame
# media < 3 - Rodou
# frequência < 75% - Rodou

'''
nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
nota3 = float(input("Informe a nota 3: "))
nota4 = float(input("Informe a nota 4: "))
freq = float(input("Informe a frequência: "))

media = (nota1 + nota2 + nota3 + nota4)/4

if freq < 75 or media <= 3:
    print("Rodou!")
else:
    if media > 3 and media < 7:
        print("Vai a exame!")
    else:
        print("Passou por média!!!")
'''   

# Calcular área do Retângulo
'''
altura = float(input("Informe a altura do retângulo: "))
largura = float(input("Informe a altura do retângulo: "))

if altura <=0 or largura <= 0:
    if altura <= 0:
        print("Informe uma altura válida!")
    if largura <= 0:
        print("Informe uma largura válida!")
else:
    if altura == largura: print("É um quadrado!")
    else: print("É um retângulo!")
'''
    
# 6) Faça um programa em python que leia o nome de 4 times de futebol que estão em
# uma semifinal. Após, leia os gols das duas partidas: time 1 x time 2 e time 3 x time 4.
# Os times vencedores devem ir para a final. Caso haja empate, deve-se perguntar ao
# usuário qual time se classificou. Por fim, deve-se ler os gols da final e mostrar qual
# time foi campeão (se empatar, perguntar quem foi campeão).

'''
time1 = input("Informe o time 1: ")
time2 = input("Informe o time 2: ")
time3 = input("Informe o time 3: ")
time4 = input("Informe o time 4: ")

partida1GolsTime1 = int(input("Partida 1 "+time1+" x "+time2+": gols do time "+time1+" ? "))
partida1GolsTime2 = int(input("Partida 1 "+time1+" x "+time2+": gols do time "+time2+" ? "))

partida2GolsTime3 = int(input("Partida 2 "+time3+" x "+time4+": gols do time "+time3+" ? "))
partida2GolsTime4 = int(input("Partida 2 "+time3+" x "+time4+": gols do time "+time4+" ? "))

winP1 = ""
winP2 = ""

if partida1GolsTime1 > partida1GolsTime2:
    winP1 = time1
else:
    if partida1GolsTime2 > partida1GolsTime1:
        winP1 = time2
    else:
        winP1 = input("Empate entre "+time1+" e "+time2+". Quem se classificou? ")

print(winP1+" passou para a final!")

if partida2GolsTime3 > partida2GolsTime4:
    winP2 = time3
else:
    if partida2GolsTime4 > partida2GolsTime3:
        winP2 = time4
    else:
        winP2 = input("Empate entre "+time3+" e "+time4+". Quem se classificou? ")
        
print(winP2+" passou para a final!")
        
partida3GolsTime1 = int(input("Final "+winP1+" x "+winP2+": gols do time "+winP1+" ? "))
partida3GolsTime2 = int(input("Final "+winP1+" x "+winP2+": gols do time "+winP2+" ? "))

campeao = ""

if partida3GolsTime1 > partida3GolsTime2:
    campeao = winP1
else:
    if partida3GolsTime2 > partida3GolsTime1:
        campeao = winP2
    else:
        campeao = input("Empate entre "+winP1+" e "+winP2+". Quem é o campeão? ")
        
print("O vencedor é "+campeao)
'''

# 7) O imposto de renda no Brasil segue as regras presentes na tabela seguinte:
    
# Crie um programa em Python que leia o rendimento mensal do usuário, qual o modelo de
# imposto (sem correção/com correção das perdas no governo Bolsonaro) e retorne o quanto
# ele deve pagar de imposto.

rendaMens = float(input("Informe a sua renda mensal: "))
modelo = int(input("Segue os modelos de imposto:\n(1) sem correção \n(2) com correção das perdas governo Bolsonaro\n(3) com correção integral \nInforme o modelo de imposto: "))

# pagar = (renda*aliquota)-parcela

pagar = 0

if modelo != 1 and modelo != 2 and modelo != 3:
    print("Informe um modelo válido!")
else:
    if modelo == 1:    
        if rendaMens >= 1903.99 and rendaMens <= 2826.65:
            pagar = (rendaMens*0.075)-142.80
        if rendaMens >= 2826.66 and rendaMens <= 3751.05:
            pagar = (rendaMens*0.15)-354.80
        if rendaMens >= 3751.06 and rendaMens <= 4664.68:
            pagar = (rendaMens*0.225)-636.13
        if rendaMens > 4664.68:
            pagar = (rendaMens*0.275)-869.36
            
    if modelo == 2:    
        if rendaMens >= 2500.45 and rendaMens <= 3712.16:
            pagar = (rendaMens*0.075)-187.54
        if rendaMens >= 3712.17 and rendaMens <= 4926.14:
            pagar = (rendaMens*0.15)-465.95
        if rendaMens >= 4926.15 and rendaMens <= 6125.99:
            pagar = (rendaMens*0.225)-835.41
        if rendaMens > 6125.99:
            pagar = (rendaMens*0.275)-1141.71
    
    if modelo == 3:    
        if rendaMens >= 4710.50 and rendaMens <= 6993.20:
            pagar = (rendaMens*0.075)-353.29
        if rendaMens >= 6993.21 and rendaMens <= 9280.19:
            pagar = (rendaMens*0.15)-877.78
        if rendaMens >= 9280.20 and rendaMens <= 11540.53:
            pagar = (rendaMens*0.225)-1573.80
        if rendaMens > 11540.53:
            pagar = (rendaMens*0.275)-2150.82
            
if pagar == 0:
    print("Isento!")
else:
    print(f"Você tem que pagar pagar R$ {pagar}")