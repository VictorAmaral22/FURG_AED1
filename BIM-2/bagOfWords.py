import re
import csv

text = '''Eu quis dar pra você (lá ele) todo o meu amor Mas ela só me quis como amante E ainda mete por trás nesse pobre rapaz que garante (lá nele) Que esse corpo gostoso é só dele e de mais ninguém Lá ele mil vezes (lá ele mil vezes) Se eu fico arriado de quatro por você? (lá ele) Vai dar merda, eu sei que eu vou me arrepender depois Um lá ele pra nós dois Lá ele Quando ela beija o seu namorado e me beija Por tabela, eu beijo ele Lá ele Deus me livre, Deus é mais Se além de beijo ela também ajoelhou pra ele Lá ele Quando ela beija o seu namorado e me beija Por tabela, eu beijo ele Lá ele Deus me livre, Deus é mais Sé além de beijo ela também ajoelhou pra ele Lá ele mil vezes Se eu fico arriado de quatro por você? (lá ele) Vai dar merda, eu sei que eu vou me arrepender depois Um lá ele pra nós dois Lá ele Quando ela beija o seu namorado e me beija Por tabela, eu beijo ele Lá ele Deus me livre, Deus é mais Sé além de beijo ela também ajoelhou pra ele Lá ele Quando ela beija o seu namorado e me beija Lá ele Deus me livre, Deus é mais Sé além de beijo ela também ajoelhou pra ele Ele achou que ia me sacanear Mas o lá ele está aqui para me salvar Ele achou que ia me sacanear Mas o lá ele está aqui para me salvar'''.lower()

text = re.sub(r'[!?\'\"“”;,.()\[\]]', '', text)
splitted = text.split(" ")

bag = []
frequency = []

for word in splitted:
    try:
        index = bag.index(word)
        if index or index == 0:
            frequency[index] = frequency[index] + 1
    except:
        bag.append(word)
        frequency.append(1)

c = 0
for word in bag:
    percent = round((frequency[c]/len(splitted))*100, 2)
    print(f"{word} - {percent}%")

    c = c + 1

# def countWords (word):
#     corresponding = 0
#     word = word.lower()
#     try:
#         index = bag.index(word)
#         if index or index == 0:
#             corresponding = frequency[index]
#             print(f"A palavra {word} se repete {corresponding} vez(es).")
#     except:
#         print("Essa palavra não está no texto!")

def writeCSV ():
    outputStr = "termo;frequênca\n"

    c = 0
    for word in bag:
        outputStr = outputStr + word+";"+str(frequency[c])+"\n"
        c = c + 1

    print(outputStr)

    f = open("bagOfWords.csv", "w")
    f.write(outputStr)
    f.close()

writeCSV()
