# 1) (5 Pontos) Imagine que você está conduzindo um experimento científico em um
# laboratório e deseja analisar os dados coletados. Os dados são representados em
# forma de listas em um arquivo texto, e você precisa criar um programa em Python
# para realizar algumas operações de análise de dados.
# O arquivo possui o seguinte formato:

    # ● 1ª linha: uma lista de temperaturas medidas em graus Celsius, separadas por vírgula.
    # ● 2ª linha: uma lista de pressões medidas em Pascal, separadas por vírgula.
    # ● 3ª linha: uma lista de nomes dos experimentos correspondentes, separados por vírgula.

# O programa deve ser capaz de ler esse arquivo e fazer o seguinte:
    # ● Calcular a temperatura média e a pressão média a partir das listas.
    # ● Identificar qual experimento teve a maior temperatura máxima.
    # ● Identificar qual experimento teve a menor pressão mínima.
    # ● Exibir todos os experimentos em que a temperatura seja superior a 25 graus Celsius.

arq = open("dados.csv", "r")
lines = arq.readlines()

formattedLines = []

c = 0
for line in lines:
    line = line.strip().split(",")
    tmpLine = []
    
    for column in line:
        if c < 2:
            tmpLine.append(float(column))
        else:
            if column != "":
                tmpLine.append(column.strip()) 
        

    formattedLines.append(tmpLine)
    c += 1

tempMedia = 0
pressMedia = 0
tempMaior = False
tempMaiorPos = False
pressMenor = False
pressMenorPos = False
superiorTemp = []

c = 0
for temperature in formattedLines[0]:
    tempMedia += temperature

    if not tempMaior:
        tempMaior = temperature
    else:
        if temperature > tempMaior:
            tempMaior = temperature
            tempMaiorPos = c

    if temperature > 25:
        superiorTemp.append(c)

    c += 1

tempMedia = tempMedia/len(formattedLines[0])

c2 = 0
for pressure in formattedLines[1]:
    pressMedia += pressure

    if not pressMenor:
        pressMenor = pressure
    else:
        if pressure < pressMenor:
            pressMenor = pressure
            pressMenorPos = c2

    c2 += 1

pressMedia = pressMedia/len(formattedLines[1])

print("A temperatura média é de "+str(tempMedia)+"° Celcius")
print("O experimento com a maior temperatura foi o "+formattedLines[2][tempMaiorPos]+", com "+str(formattedLines[0][tempMaiorPos])+"° Celcius")
print("A pressão média é de "+str(pressMedia)+" Pascal")
print("O experimento com a menor pressão foi o "+formattedLines[2][pressMenorPos]+", com "+str(formattedLines[1][pressMenorPos])+" Pascal")
print("E os seguintes experimentos tiveram temperatura superior a 25° Celcius: ")

for sup in superiorTemp:
    print(formattedLines[2][sup]+" - "+str(formattedLines[0][sup])+"° Celcius - "+str(formattedLines[1][sup])+" Pascal")