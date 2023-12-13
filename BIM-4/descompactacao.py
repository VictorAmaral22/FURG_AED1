with open ('entrada.txt', 'r') as arq:
    texto = arq.read()

print(texto)

lista = texto.split(' ')
print(lista)
cont = 0
dic = {}
zipada = []
txt_zipada = ''

for item in lista:
    if item not in dic:
        dic[item] = str(cont)
        txt_zipada += f'{item}:{dic[item]};'
        cont += 1
    zipada.append(dic[item])

print(zipada)

txt_zipada += '\n'
txt_zipada += ' '.join(zipada)
print(txt_zipada)

with open ('saida_compactada.txt', 'w') as arq:
    arq.write(txt_zipada)
