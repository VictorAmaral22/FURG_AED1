# if "penna" in "rafael penna":
#     print("sim")
# else:
#     print("não")

import testes.caseFunction as caseFunction

# Testar se tem todas as letas do alfabeto
text = input("Informe um texto: ")
text = caseFunction.minuscula(text)
text2 = caseFunction.maiuscula(text)

c = 97
found = 0

while c <= 122:
    if chr(c) in text:
        found = found + 1
    
    c = c + 1

if found != 26:
    print("Hoje não meu nobre")
else:
    print('Bem demais!')