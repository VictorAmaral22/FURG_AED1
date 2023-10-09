# 2) (5 Pontos) Você deve criar um jogo de dados em Python onde o jogador lança dois
# dados de seis faces e tenta adivinhar se a soma dos números nos dados será maior
# ou igual a um determinado valor escolhido. Implemente uma função chamada
# lançar_dados, que simula o lançamento de dois dados de seis faces (sortear) e
# retorna a soma dos resultados. Implemente uma função chamada validar_aposta,
# que verifica se a aposta do jogador é um número inteiro positivo entre 2 e 12.

# Exemplo:

# Bem-vindo ao Jogo de Dados!
# Digite o valor alvo (2-12): 7

# Lançando os dados...

# Os números nos dados somam 8.

# Você ganhou a aposta! A soma dos dados é maior ou igual a 7.

import random

def validade_resposta (num):
    if num < 2 or num > 12:
        print("Digite um valo válido, tem que ser de 2 à 12...")
        return False
    else: 
        return True
    
def lancar_dados ():
    print("Lançando dados...")
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    return dado1 + dado2

print("Bem-vindo ao Jogo de Dados!")

num = int(input("Digite o valor alvo (2-12): "))
valid = validade_resposta(num)

while not valid:
    num = int(input("Digite o valor alvo (2-12): "))
    valid = validade_resposta(num)

soma = lancar_dados()

print("Os números nos dados somam "+str(soma))

if num <= soma:
    print("Você ganhou a aposta! A soma dos dados é maior ou igual a "+str(num)+".")
else:
    print("Você perdeu, o valor é maior que a soma dos dados...")