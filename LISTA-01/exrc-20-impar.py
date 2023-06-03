# 20) Faça um programa em python que leia um valor inteiro X. Em seguida apresente os 6
# valores ímpares consecutivos a partir de X, inclusive o X se for o caso. Por exemplo,
# para o número 8, a saída será “9,11,13,15,17,19”.

imparC = 0
num = int(input("Informe um número: "))
imparString = ""
c = num

while imparC < 6:
    if c%2 != 0:
        imparC = imparC + 1
        imparString = imparString + str(c)
        
        if imparC < 6:
            imparString = imparString + ", "

    c = c + 1

print(imparString)
    

