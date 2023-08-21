# 1) (3 Pontos) Uma empresa de transporte oferece diferentes tarifas com base na distância percorrida em quilômetros e no tipo de veículo utilizado. Implemente um programa em Python que solicite ao usuário a distância da viagem e o tipo de veículo, e calcule o valor total a ser pago. As informações sobre as tarifas estão descritas a seguir: 
#     Ônibus: R$ 0,50 por Km; 
#     Carro: R$ 0,75 por Km; 
#     Moto: R$ 0,45 por Km. 

# Além disso, a empresa oferece os seguintes descontos, dependendo da distância:

# Até 100 km: nenhum desconto.
# De 101 km a 300 km: 10% de desconto.
# Acima de 300 km: 20% de desconto.

# Exemplo:
# Digite a distância da viagem (em km): 250
# Digite o tipo de veículo (ônibus, carro ou moto): carro
# Valor total a ser pago: R$ 168,75

distancia = float(input("Informe a distância da viagem em Km: "))

while distancia == 0:
    distancia = float(input("Informe uma distância válida em Km: "))
    
veiculo = input("Digite o tipo de veículo (ônibus, carro, moto): ")

while veiculo != "ônibus" and veiculo != "carro" and veiculo != "moto":
    veiculo = input("Digite o tipo de veículo válido (ônibus, carro, moto): ")

desconto = 0
valor = 0

if veiculo == "ônibus":
    valor = distancia*0.5
    
if veiculo == "carro":
    valor = distancia*0.75
    
if veiculo == "moto":
    valor = distancia*0.45


if distancia > 100 and distancia <= 300:
    desconto = (valor*10)/100
if distancia > 300:
    desconto = (valor*20)/100

valor = valor - desconto
    
print(f"Valor total a ser pago R$ {valor}")