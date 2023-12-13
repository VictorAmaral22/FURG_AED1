'''
def incrementa (x):
    print(x, id(x))
    x += 1
    print(x, id(x))
    return x

x = 15
print(x, id(x))
novo = incrementa(x)
print(novo, id(novo))
'''

list = [1, 2, 3]

print(id(list[0]))
list[0] = 2
print(id(list[0]))