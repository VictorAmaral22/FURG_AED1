# 21) Escreva um programa que leia dois valores x e y. Em seguida escreva quais são os
# números primos contidos neste intervalo. Por exemplo, para x=3 e y=14 escreva:
# 3,5,7,11,13. Verifique se o usuário digitou x e y de modo que x<y

def isPrimeNum (x):
    c = 2
    primo = x
    divisions = 0

    while c <= primo:
        if divisions > 1:
            c = primo+1
        else:
            if primo % c == 0:
                divisions = divisions + 1

            c = c + 1

    if divisions == 1:
        return True
    else:
        return False

x = int(input("Informe o começo do intervalo: "))
y = int(input("Informe o fim do intervalo: "))

while x > y:
    print("O começo do intervalo precisa ser menor que o final")
    x = int(input(f"Informe o começo do intervalo, o final é {y}: "))

c = x

numString = ""

while c <= y:
    isPrime = isPrimeNum(c)

    if isPrime:
        if numString == "":
            numString = numString + str(c)
        else:
            numString = numString + ", " + str(c)
    
    c = c + 1

print(numString)