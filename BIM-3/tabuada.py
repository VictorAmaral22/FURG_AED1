number = int(input("Informe até qual número você deseja a tabuada? "))

tabuada = []

tabuada.append(list(range(11)))

for num in range(1, number+1):
    row = [num]
    
    for mult in tabuada[0]:
        if mult > 0:
            result = num*mult
            print(str(num)+" x "+str(mult)+" = "+str(result))
            row.append(result)

    tabuada.append(row)
        

print(tabuada)

tabuadaFormated = """"""

for row in tabuada:
    res = ""
    for col in row:
        if res != "":
            res += ";"

        res += str(col)

    res += "\n"
    tabuadaFormated += res

arq = open("tabuada.csv", "w")
arq.write(tabuadaFormated)
arq.close()
