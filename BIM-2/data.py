day = int(input("Informe o dia: "))
month = int(input("Informe o mês: "))
year = int(input("Informe o ano: "))
bissexto = "false"

if year > 100 and year%100 == 00:
    if year%400 == 0:
        bissexto = "true"
else: 
    if year%4 == 0:
        bissexto = "true"
    
if day > 31 or day < 1 or month > 12 or month < 1 or year < 0:
    print("Data inválida!")
else:
    if day == 31 and (month == 4 or month == 6 or month == 9 or month == 11):
        print("Data inválida!")
    else:
        if month == 2 and ((bissexto == "false" and day > 28) or (bissexto == "true" and day > 29)):
            print("Data inválida!")
        else:
            print(f"Data válida: {day}/{month}/{year}")