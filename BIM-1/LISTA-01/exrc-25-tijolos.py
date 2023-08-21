# 25) Faça um programa em python que desenhe uma pirâmide conforme 2 dados
# informados pelo usuário. O primeiro dado indica o "tijolo" e o segundo a quantidade
# de andares.
# Ex: Informe o tijolo: A
# Informe a quantidade de andares: 5
#     A
#    AAA
#   AAAAA
#  AAAAAAA
# AAAAAAAAA

text = input("Informe o tijolo: ")
levels = int(input("Informe os andares: "))
c = 1

while c <= levels:
    print((levels-c)*" "+(text*(c*2-1)))

    c = c + 1