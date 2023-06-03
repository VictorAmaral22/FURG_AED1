# 22) Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor
# e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Faça
# um programa em Python que receba o nome do(a) ginasta, e as notas de sua
# apresentação dadas pelos sete jurados. Ao final, informe a melhor nota, a pior nota e
# a sua média final, conforme a descrição acima informada (ou seja, retirar a melhor e
# a pior nota para calcular a média). As notas não são informadas em ordem (crescente
# ou decrescente).

c = 0
maior = 0
menor = 0
somatorio = 0

while c < 7:
    nota = int(input("Informe a nota: "))
    somatorio = somatorio + nota

    if nota > maior:
        maior = nota

    if menor == 0 or nota < menor:
        menor = nota

    c = c + 1

media = (somatorio-maior-menor)/5

print(f"Melhor nota {maior}")
print(f"Pior nota {menor}")
print(f"Média final {media}")