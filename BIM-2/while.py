country = "França"
tentativa = input("Informe um páis (você tem 5 tentativas): ")
c = 4

while tentativa != country and c >= 1:
    print(f"Errouuu! Restam {c} tentativas.. ")
    
    tentativa = input("Informe um páis: ")
    c -= 1

if tentativa != country and c < 1:
    print("Suas chances acabaram...")
else:
    print("Acertou. O país é "+tentativa)