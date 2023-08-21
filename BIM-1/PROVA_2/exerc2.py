# 2) (3,5 Pontos) Crie um programa em Python que imprima uma sequência de números
# em forma de pirâmide. O programa deve solicitar ao usuário um número inteiro
# positivo e, em seguida, imprimir os números de 1 até o número informado, em linhas
# crescentes e decrescentes, formando uma pirâmide.
# Exemplo:
# Digite um número inteiro positivo: 4
# 1
# 12
# 123
# 1234
# 4321
# 321
# 21
# 1

num = int(input("Digite um número inteiro positivo: "))
c = 0
stringCres = ""
stringDesc = ""

while c < num:
    stringCres = stringCres + str(c+1)
    stringDesc = str(c+1) + stringDesc 
    c = c + 1
    print(stringCres)
    

while c > 0:
    if c != num:
        c1 = c
        desc = ""
        while c1 > 0:
            desc = desc + str(c1)
            c1 = c1 - 1
        
        stringDesc = desc
        
    c = c - 1        
    print(stringDesc)