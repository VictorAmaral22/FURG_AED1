# 15) Escreva um programa que mostre a sequência de Fibonacci até o enésimo termo (n
# deve ser informado pelo usuário). A sequência de Fibonacci é aquela em que cada
# termo é a soma dos dois termos anteriores. Por exemplo, para n=8 escreva 0, 1, 1, 2,
# 3, 5, 8 e 13.

# Fn = Fn-1 + Fn-2

num = int(input("Informe um número: "))

def Fibonacci (x):
    first = 1
    second = 1

    print(0)
    if x == 1:
        print(1)

    if x == 2:
        print(1)
        print(1)

    if x > 2:
        print(1)
        print(1)

        c = 2
        third = 0

        while c < x:
            third = first + second
            first = second
            second = third
            print(third)

            c = c + 1
        
Fibonacci(num)