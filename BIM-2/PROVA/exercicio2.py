# 2) (5 Pontos) O Instagram é uma popular plataforma de mídia social que permite aos
# usuários compartilhar fotos e vídeos. Considere um cenário em que você está
# desenvolvendo uma funcionalidade para analisar os comentários em postagens do
# Instagram.

# a) Escreva um código em Python que verifique se uma string comentário contém a
# menção a um usuário. Uma menção começa com o símbolo "@" seguido por um
# nome de usuário válido (composto apenas por letras minúsculas e números), por
    # exemplo: "@usuario123".

# b) Escreva um código em Python que substitua todas as menções a usuários na string
# comentário por "USUARIO_MENCIONADO".

# c) Dado um conjunto de palavras proibidas, escreva um código em Python que
# verifique se a string comentário contém alguma das palavras proibidas. Se contiver,
# exiba "Conteúdo inadequado", caso contrário, exiba "Comentário permitido".

chars = "1234567890aáàẫãbcdeéèêẽfghiíìĩîjklmnoóòõôpqrstuúùũûvwxyz"
forbiddenTerms = ["palavra maldosa 1", "palavramaldosa2", "palavra maldosa3", "palavramaldosa 4"]

comment = input("Informe o comentário: ")
words = comment.split(" ")
newComment = ""

hasMention = 0
for word in words:
    position = word.find("@")
    if position == 0 and len(word) > 1 and (word[position+1] in chars):
        hasMention = 1
        returnStr = "USUARIO_MENCIONADO"
        for letter in word:
            if letter != "@" and not letter in chars:
                returnStr = returnStr + letter
        
        newComment = newComment + returnStr + " "
    else:
        newComment = newComment + word + " "
        
hasForbidden = 0

for term in forbiddenTerms:
    if "".join(newComment.lower().split(" ")).find("".join(term.split(" "))) != -1:
        hasForbidden = 1


if hasMention == 1:
    print("Tem menção!")
else: 
    print("Não tem menção!")

if hasForbidden == 0:
    print("Conteúdo permitido")
    print(newComment)
else: 
    print("Conteúdo inadequado")