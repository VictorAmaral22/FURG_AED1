nome = input("Informe o nome: ")
matricula = input("Informe o número de matrícula: ")
nota = input("Informe a nota: ")


arq = open("notas.txt", 'r')
# texto = arq.read() # lê tudo, ou com read(3) lê até o terceiro char
# print(texto)

# linha = arq.readline() 
# print(linha)

lista1 = arq.readlines()
print(lista1) # ['Victor Amaral;162650;10\n', 'Rodrigo Goes;162651;10']
arq.close()

arq2 = open('notas2.txt', 'w')
texto = nome+";"+str(matricula)+";"+str(nota)+"\n"
arq2.write(texto)
arq2.close()