# Exrc 1

'''
products = [
    { "id": 1, "name": "Cachorro Quente", "price": 4.0 },
    { "id": 2, "name": "X-Salada", "price": 4.5 },
    { "id": 3, "name": "X-Bacon", "price": 5.0 },
    { "id": 4, "name": "Torrada Simples", "price": 2.0 },
    { "id": 5, "name": "Refrigerante", "price": 1.5 },
]

product, qtd = [int(x) for x in input().strip().split(' ')]

total = 0

for prod in products:
    if prod["id"] == product:
        total = prod["price"]*qtd

print(f"Total: R$ {total:.2f}")
'''

# Exrc 2

'''
vert = input()
category = input()
food = input()

animal = {
    "vertebrado": {
        "ave": {
            "carnivoro": "aguia",
            "onivoro": "pomba",
        },
        "mamifero": {
            "herbivoro": "vaca",
            "onivoro": "homem",
        },
    },
    "invertebrado": {
        "inseto": {
            "hematofago": "pulga",
            "herbivoro": "lagarta",
        },
        "anelideo": {
            "hematofago": "sanguessuga",
            "onivoro": "minhoca",
        },
    },
}

print(animal[vert][category][food])
'''

# Exrc 3

'''
ddd = { 
    "61": "Brasilia",
    "71": "Salvador",
    "11": "Sao Paulo",
    "21": "Rio de Janeiro",
    "32": "Juiz de Fora",
    "19": "Campinas",
    "27": "Vitoria",
    "31": "Belo Horizonte" 
}

number = input()

if number in ddd:
    print(ddd[number])
else:
    print("DDD nao cadastrado")

'''

# Exrc 4

casos = int(input())

for caso in range(casos):
    produtos = int(input())

    precos = {}

    for prod in range(produtos):
        fruta, preco = input().strip().split(' ')

        precos[fruta] = float(preco)

    compras = int(input())

    total = 0.0
    for prod in range(compras):
        fruta, quantidade = input().strip().split(' ')

        total += int(quantidade) * precos[fruta]

    print(f'R$ {total:.2f}')
