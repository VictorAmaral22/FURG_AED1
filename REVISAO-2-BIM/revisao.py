# strings
nome = "Rafael"
# nome[3] = 'b' NÃO PODE ATRIBUIR
print(nome[3])
print(nome)
cont = 0
while cont<len(nome):
    print(cont)
    cont = cont + 1

for letra in nome:
    print(letra)

nome.lower() # rafael
print(ord("A"))
print(chr(97))

# listas
lista1 = [1, 2, 3, "André"]
'''
print(lista1)
for elem in lista1: 
    print(elem)
'''

lista1[3] = "Penna"
lista1.append("Novo")

print(lista1)