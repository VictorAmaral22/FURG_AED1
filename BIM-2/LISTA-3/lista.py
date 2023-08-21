# 1) Crie uma lista com números aleatórios (pelo menos 5 elementos) e crie um menu interativo que permita ao usuário escolher as seguintes opções:
#     -Ver a lista completa
#     -Ver a soma dos elementos da lista
#     -Ver o maior número da lista
#     -Ver o menor número da lista
#     -Ver a média dos elementos da lista
# O menu deve se repetir até que o usuário escolha sair.


# 2) Crie uma lista de nomes de cidades. Peça ao usuário para digitar o nome de uma cidade e verifique se ela está presente na lista. 
# Se estiver, remova a cidade da lista e imprima a lista resultante. Caso contrário, imprima uma mensagem dizendo que a cidade não foi encontrada. 
# Faça 2 versões desse exercício, uma usando a função “remove” e outra sem usar funções prontas do python.


# 3) Crie 3 listas que contém o nome de um produto, o seu preço e a quantidade disponível em estoque. 
# Peça ao usuário para comprar um produto digitando o nome e a quantidade desejada. 
# Verifique se o produto está disponível em estoque e, se estiver, atualize a quantidade disponível e informe o total a pagar. 
# Repita esse processo até que o usuário digite "sair".

'''
products = [
    "Jogo Assassin's Creed Brotherhood",
    "Jogo Baldur's Gate 3",
    "Jogo The Witcher 3",
]
price = [
    10.90,
    199.90,
    25.00,
]
quantity = [
    4,
    10,
    5,
]

cart = []
total = 0
search = input("Bem vindo a gaming store! O que você deseja? ")
while search != "sair":
    if search != "":
        options = ""
        c = 0
        for prod in products:
            if search.lower() in prod.lower():
                options = options + "["+str(c)+"] - "+prod+" ("+str(quantity[c])+" disponíveis) R$ "+str(price[c])+"\n"
            c = c + 1
        
        if(options == ""):
            print("Não temos nenhum produto com esse nome!")
            search = ""
        else:
            print(options)
            buy = int(input("Qual desses você deseja? "))
            
            while quantity[buy] == 0:
                buy = int(input("Esse produto não está disponível, escolha outro... "))

            add = ""
            while add != "sim" and add != "não":
                add = input("Deseja comprar esse produto "+products[buy]+" R$ "+str(price[buy])+" ? ")
                if add == "sim":
                    qtd = int(input("Informe a quantidade desejada: max "+str(quantity[buy])+" "))
                    while qtd > quantity[buy] or qtd == 0:
                        qtd = int(input("Informe uma quantidade válida: max "+str(quantity[buy])+" "))
                    
                    total = total + (qtd*price[buy])
                    cart.append(products[buy]+" ("+str(qtd)+") R$ "+str(price[buy]))

                    tmpQuantity = []
                    c2 = 0
                    for item in quantity:
                        if c2 == buy:
                            tmpQuantity.append(quantity[buy]-qtd)
                        else:
                            tmpQuantity.append(quantity[c2])
                        c2 = c2 + 1
                    quantity = tmpQuantity
                search = ""
    else: 
        print("Total do carrinho "+str(len(cart))+": "+str(total))
        search = input("O que mais você deseja? ")

print("Seu carrinho: ")
for item in cart:
    print(item)
print("Total: "+str(total))
'''

# 4) Crie um programa que recebe uma string como entrada e retorna uma nova string em que cada caractere foi substituído pelo seu código ASCII.
# Exemplo:
# Informe o texto: Hello
# Saída esperada: "72 101 108 108 111"

'''
string = input("Conte o seu segredo: ")
words = string.split(" ")

encoded = ""

for word in words:
    c = 0
    while c < len(word):
        encoded = encoded + str(ord(word[c])) + " "
        c = c + 1

    encoded = encoded + " "

print(encoded)
'''

# 5) Crie um programa que leia uma string e um número inteiro como chave e retorne uma nova string em que cada caractere 
# foi deslocado para a direita na sequência de caracteres ASCII pelo valor da chave. 
# Exemplo:
# Informe a mensagem: hello
# Informe a chave: 3
# Saída esperada: "khoor"

'''
string = input("Conte o seu segredo: ").lower()
key = int(input("Qual é a chave? "))
words = string.split(" ")

encoded = ""

for word in words:
    c = 0
    while c < len(word):
        encoded = encoded + chr(ord(word[c])+key)
        c = c + 1

    encoded = encoded + " "

print(encoded)
'''

# 6) Crie um programa que recebe uma string com letras maiusculas, espaços e números como entrada e retorna uma nova string em que cada caractere foi convertido para o código Morse.			Código Morse:
# Exemplo:
# Informe a mensagem: HELLO 123
# Saída esperada: ".... . .-.. .-.. ---   .---- ..--- ...--"

'''
morseCodes = [
    ["a", ".-"],
    ["b", "-..."],
    ["c", "-.-."],
    ["d", "-.."],
    ["e", "."],
    ["f", "..-."],
    ["g", "--."],
    ["h", "...."],
    ["i", ".."],
    ["j", ".---"],
    ["k", "-.-"],
    ["l", ".-.."],
    ["m", "--"],
    ["n", "-."],
    ["o", "---"],
    ["p", ".--."],
    ["q", "--.-"],
    ["r", ".-."],
    ["s", "..."],
    ["t", "-"],
    ["u", "..-"],
    ["v", "...-"],
    ["w", ".--"],
    ["x", "-..-"],
    ["y", "-.--"],
    ["z", "--.."],

    ["1", ".----"],
    ["2", "..---"],
    ["3", "...--"],
    ["4", "....-"],
    ["5", "....."],
    ["6", "-...."],
    ["7", "--..."],
    ["8", "---.."],
    ["9", "----."],
    ["0", "-----"],
]

string = input("Informe o texto secreto: ").lower()
words = string.split(" ")

encoded = ""

for word in words:
    c = 0
    while c < len(word):
        for code in morseCodes:
            if(code[0] == word[c]):
                encoded = encoded + code[1] + " "
        c = c + 1

    encoded = encoded + "   "

print(encoded)
'''