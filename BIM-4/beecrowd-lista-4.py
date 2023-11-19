# Exrc 1

'''
products = [
    [1, "Cachorro Quente", 4.0],
    [2, "X-Salada", 4.5],
    [3, "X-Bacon", 5.0],
    [4, "Torrada Simples", 2.0],
    [5, "Refrigerante", 1.5],
]

product, qtd = [int(x) for x in input().strip().split(' ')]

total = 0

for prod in products:
    if prod[0] == product:
        total = prod[2]*qtd

print(f"Total: R$ {total:.2f}")
'''

# Exrc 2

'''
vert = input()
category = input()
food = input()

if vert == "vertebrado":
    if category == "ave":
        if food == "carnivoro":
            print("aguia")
        if food == "onivoro":
            print("pomba")
    if category == "mamifero":
        if food == "herbivoro":
            print("vaca")
        if food == "onivoro":
            print("homem")
else:
    if category == "inseto":
        if food == "hematofago":
            print("pulga")
        if food == "herbivoro":
            print("lagarta")
    if category == "anelideo":
        if food == "hematofago":
            print("sanguessuga")
        if food == "onivoro":
            print("minhoca")
'''

# Exrc 3

'''
ddd = [
    [61, "Brasilia"],
    [71, "Salvador"],
    [11, "Sao Paulo"],
    [21, "Rio de Janeiro"],
    [32, "Juiz de Fora"],
    [19, "Campinas"],
    [27, "Vitoria"],
    [31, "Belo Horizonte"],
]

number = int(input())

city = ""

for d in ddd:
    if d[0] == number:
        city = d[1]
        break
        
if city == "":
    print("DDD nao cadastrado")
else:
    print(city)
'''

# Exrc 4

cases = int(input())

for case in range(cases):
    frase = input().strip().lower()

    freq = []
    letters = []
    
    for letra in frase:
        if(letra in "abcdefghijklmnopqrstuvwxyz"):
            if letra in letters:
                freq[letters.index(letra)][1] += 1
            else:
                letters.append(letra)
                freq.append([
                    letra,
                    1
                ])
    
    maior = 0
    for letra in freq:
        if letra[1] > maior:
            maior = letra[1]
    
    resposta = []
    for letra in freq:
        if(letra[1] == maior):
            resposta.append(letra[0])
    
    resposta.sort()
    print(''.join(resposta))
