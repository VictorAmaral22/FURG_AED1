# 24) Construa um programa em Python que escreva uma contagem de 10 (dez) minutos,
# ou seja, mostre 0:00, e então 0:01, 0:02, ..., 0:58, 0:59, 1:00, 1:01, ..., até 10:00

min = 0
hrs = 0

while min/60 <= 10:
    minutesF = (min-((min//60)*60))
    hoursF = min//60

    if minutesF < 10:
        minutesF = "0"+str(minutesF)

    if hoursF < 10:
        hoursF = "0"+str(hoursF)
    
    print(f"{hoursF}:{minutesF}")

    min = min + 1
