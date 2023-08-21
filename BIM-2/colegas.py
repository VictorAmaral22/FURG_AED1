import random
random.seed()

colegas = [ 
    "Victor", "Christian", "Murilo", "Marina", "Bruno dos Santos", 
    "Sabrina", "Éshley", "Érick", "Andrew", "Augusto", "Aythana", 
    "Babi", "Bernardo", "Bruno", "CB", "Duds", "Fabi", "Felipe", 
    "Henrique", "Lucas", "Paula", "Thiago", "Vicenzo", "Arthur",
    "Duda", "Gabriel Pinheiro", "Gabriel Viana", "John Kennedy", "Medina", 
    "Tiago Pinheiro", "Vitória", "Milena"
]
sorteados = []
premios = ["Notebook gamer", "Duas estradas show da Taylor Swift", "Creatina + Whey Protein", "Viagem pro Paraguai", "Abacaxi"]

c = 0

while c < 5:
    index = random.randint(0, len(colegas)-1)
    
    while colegas[index] in sorteados:
        index = random.randint(0, len(colegas)-1)

    print(f"{colegas[index]} ganhou {premios[c]}")
    sorteados.append(colegas[index])

    c = c + 1

