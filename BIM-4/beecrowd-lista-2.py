# Exrc 1 
# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. 
# Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. 
# Este é apenas um exercício com objetivo de testar raciocínio matemático simples. 

idadeEmDias= int(input(""))

anos = 0
meses = 0
dias = 0

anos = idadeEmDias//365
meses = (idadeEmDias%365)//30
dias = (idadeEmDias%365)%30

print(str(anos)+" ano(s)")
print(str(meses)+" mes(es)")
print(str(dias)+" dia(s)")