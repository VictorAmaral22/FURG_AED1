from PIL import Image

im = Image.open('mario.png')
pix = im.load()
size = list(im.size)
print(size)
print(pix[10,10])

table = """
    <table>
"""

for row in range(int(size[0])):
    table += "<tr>"
    for col in range(int(size[1])):
        table += f"<td style=\"background-color: rgb{str(pix[row,col])}\"></td>"
    table += "</tr>"

im.close()

table += "</table>"

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        {"td { width: 1px; height: 1px; }"}
    </style>
</head>
<body>
    <div classname="grid">
        {table}
    </div>
</body>
</html>
"""

arq = open("image.html", "w")
arq.write(html)
arq.close()