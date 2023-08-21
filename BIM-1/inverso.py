num = int(input("Manda um número meu consagrated: "));
cen = num//100
dez = (num%100)//10
un = num%10

invert = (un*100 + dez*10 + cen)

'''
print([cen, dez, un])
'''
print("Baita ",invert)
