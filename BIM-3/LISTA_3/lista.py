# 1) Faça um programa em Python para ler “n” números inteiros, armazenando-os em uma
# lista (o usuário informará um valor inteiro positivo para “n”). Após, crie duas outras listas a
# partir desta primeira digitada, sendo que uma conterá os números positivos (>= 0), e a outra
# conterá os números negativos. Mostre na tela como ficaram as três listas.

'''
n = int(input("Informe a quantidade de números inteiros: "))
c = 0
integersList = []
positiveList = []
negativeList = []

while c < n:
    number = int(input("Informe o "+str(c+1)+"° número inteiro: "))
    integersList.append(number)

    if number < 0:
        negativeList.append(number)
    else:
        positiveList.append(number)

    c += 1
'''

'''
print("A lista original: "+str(integersList))
print("Números positivos: "+str(positiveList))
print("Números negativos: "+str(negativeList))
'''

# 2) Baseado no programa anterior, remova todas as ocorrências do valor zero na lista dos
# números positivos. Mostre na tela as três listas, informando a quantidade de zeros que
# havia, o total de números remanescentes na lista de positivos e na de negativos.

'''
zeroCounter = 0
zeroCounterPositive = 0
zeroCounterNegative = 0

newIntegersList = []
newPositiveList = []
newNegativeList = []

for value in integersList:
    if value == 0:
        zeroCounter += 1
    else:
        newIntegersList.append(value)

for value in positiveList:
    if value == 0:
        zeroCounterPositive += 1
    else:
        newPositiveList.append(value)

for value in negativeList:
    if value == 0:
        zeroCounterNegative += 1
    else:
        newNegativeList.append(value)

print("A lista original: tinha "+str(zeroCounter)+" zeros, sobraram "+str(len(newIntegersList))+" "+str(newIntegersList))
print("Números positivos: tinha "+str(zeroCounterPositive)+" zeros, sobraram "+str(len(newPositiveList))+" "+str(newPositiveList))
print("Números negativos: tem "+str(len(newNegativeList))+" números em "+str(newNegativeList))
'''

# 3) Faça um programa em Python que crie uma matriz de inteiros de cinco linhas por dez
# colunas. Leia os valores desta matriz linha após linha, e exiba a matriz na tela coluna por
# coluna.

'''
matrix = []

for row in range(5):
    rowArr = []
    for column in range(10):
        rowArr.append(column)

    matrix.append(rowArr)

for row in matrix:
    rowStr = "| "
    for column in row:
        rowStr += str(column)+" "
    rowStr += "|"
    print(rowStr)
''' 

# 4) Faça uma função em Python que receba, por parâmetro, um número inteiro x > 0, e
# retorne o número de divisores positivos que x tem. Por exemplo: o número 12 tem 6
# divisores (1, 2, 3, 4, 6 e 12).


# 5) Faça uma função em Python para calcular X elevado à Y, ou X Y. 
# A função deverá receber, por parâmetro, X e Y, e retornar o resultado da chamada da subrotina. 
# Exemplo: 2 elevado à 3 é igual à 2*2*2 = 8. Os parâmetros são 2 e 3, e o retorno será 8. Obs: implementar
# exatamente como no exemplo, ou seja, a exponenciação deve ser calculada por
# multiplicações sucessivas.


# 6) Faça um programa em Python que leia duas listas de números compostas por cinco
# elementos informados de maneira ordenada (números em ordem crescente). Crie uma
# terceira lista também ordenada, sendo a união das duas primeiras listas. Exiba as listas, e a
# soma dos seus elementos contidos.


# 7) Altere o programa anterior para desprezar os números iguais, caso estes existam.
# Portanto, a lista final não deve possuir números iguais armazenados.


# 8) Faça um programa em Python que leia três listas compostas por cinco números fornecidos
# pelo usuário. Crie uma matriz que reúna estas três listas (as listas podem ser as linhas ou as
# colunas da matriz). Apresente o conteúdo da matriz, assim como o seu maior valor contido


# 9) Faça um programa em Python para jogar o “jogo da velha”. O algoritmo deve permitir que
# dois jogadores joguem uma partida, usando o computador para ver o tabuleiro. Cada
# jogador vai alternadamente informando a posição onde deseja colocar a sua peça (‘O’ ou
# ‘X’). O programa deverá impedir jogadas inválidas, e determinar automaticamente quando o
# jogo terminou, e quem foi o vencedor (jogador1 ou jogador2). A cada nova jogada, o
# programa deve atualizar a situação do tabuleiro na tela.


# 10) Escreva um programa em Python que calcule o comprimento da mais longa sequência de
# espaços em branco em uma string lida.


# 11) Implementar um programa para somar matrizes.
# Obs.: as matrizes obrigatoriamente têm a mesma dimensão.


# 12) Implementar um programa para multiplicar matrizes.
# Obs (nro de elementos em cada dimensão):
# 1ª matriz = (Linhas1 x Colunas1)
# 2ª matriz = (Linhas2 x Colunas2)
# Multiplicação: (Linhas1 x Colunas1) x (Linhas2 x Colunas2), onde Colunas1 = Linhas2
# Resultado: (Linhas1 x Colunas2)


# 13) Faça uma função, em Python, cujo protótipo é QuantosDias(dia, mes, ano),
# que retorne a quantidade de dias do ano até a data informada por parâmetro. Para tanto, é
# preciso verificar o número de dias em cada mês. O mês de fevereiro pode ter 28 ou 29 dias,
# dependendo se o ano for bissexto (verificar).


# 14) Um anagrama é uma espécie de jogo de palavras, resultando do rearranjo das letras de
# uma palavra ou frase para produzir outras palavras, utilizando todas as letras originais
# exatamente uma vez. Um exemplo conhecido é o nome da personagem “Iracema”, um
# anagrama de “América”, no romance de José de Alencar. Escreva um programa, em Python,
# para ler um valor N correspondente ao número de palavras a serem informadas. Após, ler as
# N palavras, e dizer se formam um anagrama. Considerar 1 <= N <= 5, e palavras com, no
# máximo, 10 caracteres.


# 15) Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma certa cidade,
# em um determinado dia. Em um arquivo texto é fornecido, para cada casa visitada, o
# número do canal (4, 5, 7, 12) e o número de pessoas que o estavam assistindo naquela casa,
# separados por ponto e vírgula. Se a televisão estivesse desligada, nada era anotado, ou seja,
# esta casa não entrava na pesquisa. Faça uma função, em Python, que receba dois
# parâmetros, o nome do arquivo com os dados e o número do canal, e retorne a
# porcentagem de audiência deste canal.


# 16) Uma universidade deseja fazer um levantamento a respeito de seu processo de seleção.
# Para cada curso, é fornecido um arquivo texto com o seguinte conjunto de valores:
# Nome do curso;
# Código do curso;
# Número de vagas;
# Número de candidatos do sexo masculino;
# Número de candidatos do sexo feminino
# Fazer um programa em Python que:
# • Calcule e escreva, para cada curso, o número de candidatos por vaga e a porcentagem de
# candidatos do sexo feminino (escreva também o código correspondente do curso);
# • Determine o maior número de candidatos por vaga e escreva esse número juntamente
# com o código do curso correspondente (supor que não haja empate);
# • Calcule e escreva o total de candidatos.


# 17) Crie as seguintes listas derivadas da lista informada:
# L = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# ● Intervalo de 1 a 9
# ● Intervalo de 8 a 13
# ● Números pares
# ● Números ímpares
# ● Lista reversa


# 18) Faça um programa em Python que receba a temperatura média de cada mês de um
# determinado ano, e armazene-as em uma lista. Em seguida, calcule a média anual das
# temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da
# média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 –
# Fevereiro, . . . ).


# 19) A Furg está tendo problemas de espaço em disco no seu servidor de arquivos. Para
# tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço
# ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um
# programa obtido na Internet, ele conseguiu gerar o seguinte arquivo, chamado
# "usuarios.txt":

# alexandre 456123789
# anderson 1245698456
# antonio 123456456
# carlos 91257581
# cesar 987458
# rosemary 789456125

# Neste arquivo, o nome do usuário possui exatamente 15 caracteres. A partir deste arquivo,
# você deve criar um programa em Python que gere um relatório, chamado "relatório.txt", no
# seguinte formato:

# Furg Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr. Usuário Espaço utilizado % do uso
# 1 alexandre 434,99 MB 16,85%
# 2 anderson 1187,99 MB 46,02%
# 3 antonio 117,73 MB 4,56%
# 4 carlos 87,03 MB 3,37%
# 5 cesar 0,94 MB 0,04%
# 6 rosemary 752,88 MB 29,16%

# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB

# A conversão do espaço ocupado em disco, de bytes para megabytes, deverá ser feita através
# de uma função separada, que será chamada pelo programa principal. O cálculo do
# percentual de uso também deverá ser feito através de uma função, que será chamada pelo
# programa principal.


# 20) Faça um programa em Python que simule um lançamento de um dado. Lance o dado
# 100 vezes e armazene os resultados em uma lista. Depois, mostre quantas vezes cada valor
# foi conseguido. Use uma lista para armazenar os resultados da contagem de cada valor (1-6)
# e uma função para gerar números aleatórios, simulando os lançamentos do dado.


# 21) Crie uma função em Python que receba por parâmetro uma string e uma letra. Retorne a
# string equivalente à enviada como parâmetro, mas sem a letra informada. Por exemplo:
# retira(“Antonia Piedade”,”a”) —> “ntoni Piedde”
# ● Crie a função usando qualquer recurso Python, como split, search e etc;
# ● Crie a função usando apenas recursos básicos, sem as funções para manipulação de
# strings.


# 22) Crie uma função em Python que receba por parâmetro uma lista e uma letra. Retorne
# uma lista equivalente à enviada como parâmetro, mas sem a letra informada. A ordem dos
# elementos deve ser mantida. Por exemplo:
# retira([a,b,c,a,f,a,a,k],a) —> [b,c,f,k]


# 23) Dado o código abaixo, responda:
# x = 10
# y = 10
# print("x = ", x, "\n")
# print("1o print - Endereço de x", id(x))
# print("2o print - Endereço de y", id(y))
# x -= 1
# print("x = ", x, "\n")
# print(x)
# print("3o print - Endereço de x", id(x))

# a) Os endereços apresentados na tela das variáveis nos 1o e 2o prints são iguais? Por que?
# b) De acordo com a resposta no item (a), qual será o endereço apresentado no 3o print do
# código?


# 24) Dado o código abaixo, responda:
# str = "Algoritmo e Estrutura de "
# print(str)
# print("1o print - Endereço de str", id(str))
# str += "Dados"
# print(str)
# print("2o print - Endereço de str", id(str))
# Os endereços apresentados na tela são os mesmos? Por que?


# 25) Dado o seguinte código:
# def step(x,value):
# x = x + value
# print("2o print - Endereço de x", id(x))
# cont = 0
# print("1o print - Endereço de cont", id(cont))
# while cont < 10:
# step(cont,1)
# print("3o print - Endereço de cont", id(cont))
# print(cont)
# O código executará até o final (últimos prints)? Se não, como tu resolverias alterando o
# mínimo, valendo-se do conhecimento sobre ponteiros em Python?