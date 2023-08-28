arq = open("./dados.csv", "r")

htmlStart = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        td, th {
            border: 1px solid black;
            border-collapse: collapse;
        }
    </style>
</head>
<body>
"""

htmlEnd = """
</body>
</html>
""" 

data = arq.readlines()
arq.close()

print(data)

table = """
<table>\n
"""

year = input("Diga um ano para filtragem: ")

c = 0
for row in data:
    
    columns = row.split(";")
    print(columns[5])

    if c == 0 or (c > 0 and int(columns[5].replace("\n", "")) == int(year)):
        table = table + "<tr>\n"
        for col in columns:
            
            col = col.replace("\n", "")

            if col == "":
                col = "-"

            if c == 0:
                table = table + "<th>"+col+"</th>\n"
            else: 
                table = table + "<td>"+col+"</td>\n"

        table = table + "</tr>\n"    

    c = c + 1
        

table = table + "</table>\n"

html = htmlStart + table + htmlEnd
print(html)

output = open("index.html", "w")
output.write(html)

output.close()
