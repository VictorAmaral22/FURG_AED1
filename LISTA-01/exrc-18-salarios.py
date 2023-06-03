# 18) Escreva um programa que leia diversos funcionários e seu respectivo salario, ate que
# o nome de um funcionário seja “fim”. Em seguida escreva:
# a) O nome do funcionário com maior salário
# b) O nome do funcionário com menor salário
# c) A média dos salários digitados

c = 0
maiorSalNome = ""
maiorSalVal = 0

menorSalNome = ""
menorSalVal = 0

funcionario = ""
somatorio = 0

while funcionario != "fim":
    funcionario = input("Informe o nome do funcionário: ")

    if funcionario != "fim":
        sal = float(input(f"Informe o salário do funcionário {funcionario}: "))

        if sal > maiorSalVal:
            maiorSalNome = funcionario
            maiorSalVal = sal
        
        if menorSalVal == 0:
            menorSalNome = funcionario
            menorSalVal = sal
        else:
            if sal < menorSalVal:
                menorSalNome = funcionario
                menorSalVal = sal

        somatorio = somatorio + sal
        c = c + 1

print(f"O maior salário é de {maiorSalNome}, R$ {maiorSalVal}")
print(f"O menor salário é de {menorSalNome}, R$ {menorSalVal}")
print(f"A média salarial é de R$ {somatorio/c}")
