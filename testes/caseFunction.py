def minuscula (texto):
    c = 0
    newStr = ""
    while c < len(texto):
        if ord(texto[c]) >= 65 and ord(texto[c]) <= 90:
            newStr = newStr + chr(ord(texto[c])+32)
        else:
            if ord(texto[c]) >= 192 and ord(texto[c]) <= 221:
                newStr = newStr + chr(ord(texto[c])+32)
            else:
                newStr = newStr + texto[c]

        c = c + 1

    return newStr

def maiuscula (texto):
    c = 0
    newStr = ""
    while c < len(texto):
        if ord(texto[c]) >= 97 and ord(texto[c]) <= 122:
            newStr = newStr + chr(ord(texto[c])-32)
        else:
            if ord(texto[c]) >= 224 and ord(texto[c]) <= 255:
                newStr = newStr + chr(ord(texto[c])-32)
            else:
                newStr = newStr + texto[c]

        c = c + 1

    return newStr