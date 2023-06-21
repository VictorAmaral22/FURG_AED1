import sys
sys.path.insert(1, '../')
import caseFunction

# 1) Faça um programa em python que leia uma frase e a passe para maiúscula. Você não
# deve utilizar as funções prontas do python para converter para maiúscula ou minúscula.

# 2) Faça um programa em python que leia uma frase e passe para maiúscula a primeira letra
# de cada palavra. Você não deve utilizar as funções prontas do python para converter
# para maiúscula ou minúscula.

# 3) Escreva um programa que recebe uma string do usuário e imprime a string invertida.


# 4) Escreva um programa que recebe uma string do usuário e imprime a string com todas as
# letras maiúsculas convertidas para minúsculas e vice-versa.

# 5) Escreva um programa que recebe uma frase do usuário e conta o número de palavras na
# frase.


# 6) Faça um programa em python que diga se uma senha digitada é fraca, média ou forte.
#     ● Senha fraca: não possui caracteres especiais, nem letras maiúsculas.
#     ● Senha média: possui letras minúsculas, números e caracteres especiais, mas não possui letras maiúsculas.
#     ● Senha forte: possui letras minúsculas/maiúsculas, números e caracteres especiais.

senha = input("Digita a senha ai meu nobre: ")

strong = 1

hasLetters = False
hasUpperCased = False
hasSpecialChars = False
hasNumbersChars = False

specialChars = "!@#$%&*()-_+=,<.>;:/|\[]{} "

c = 65
while c <= 90 and (not hasLetters or not hasUpperCased):
    if chr(c) in senha or chr(c+32) in senha:
        hasLetters = True

        if chr(c) in senha:
            hasUpperCased = True

    c = c + 1

c2 = 0
while c2 < len(specialChars) and not hasSpecialChars:
    if specialChars[c2] in senha:
        hasSpecialChars = True

    c2 = c2 + 1

c3 = 0
while c3 <= 9 and not hasNumbersChars:
    if str(c3) in senha:
        hasNumbersChars = True

    c3 = c3 + 1

print(hasLetters)
print(hasUpperCased)
print(hasSpecialChars)
print(hasNumbersChars)

if hasLetters:
    if hasUpperCased and hasSpecialChars and hasNumbersChars:
        print("Senha forte!")
    else:
        print("Senha fraca!")
else:
    print("Você falhou miseravelmente... num gostuei")


# 7) Escreva um programa em python que leia um texto e diga se é ou não um palíndromo
# (ou seja, se o inverso da string é igual a ela). Não será possível utilizar qualquer função
# no python que trabalhe com strings.

# Exemplos:
# Ama
# Mirim
# A grama é amarga

'''
text = input("Palíndromo: ")
fText = caseFunction.minuscula(text)
f2Text = ""
inText = ""

c = 0

while c < len(fText):
    if fText[c] != " ":
        f2Text = f2Text + fText[c]
        inText = fText[c] + inText

    c = c + 1   

if f2Text == inText:
    print("É palíndromo!")
else:
    print("Não é!")
'''

# 8) Faça um programa em python que:
#     ● Crie uma senha aleatória de 6 caracteres alfanuméricos (A..Z,0..9);
#     ● Descubra a senha criada (força bruta - tentar todas possibilidades). Obs: para
# encontrar a senha, você não pode comparar pedaços da senha, precisa comparar
# toda senha (ex: if senha_gerada==senha_tentada: ).

# 9) Escreva um programa em python que leia uma string, e substitua cada segmento de dois
# ou mais espaços em branco por um só caractere de espaço. Não deve ser utilizada
# qualquer função no python que trabalhe com strings.

# 10) Faça um programa em python que leia três textos. O programa deve imprimir o primeiro
# texto substituindo todas as ocorrências do segundo pelo terceiro. Não deve ser utilizada
# qualquer função no python que trabalhe com strings.