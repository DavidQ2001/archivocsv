"""#valores separados por coma
import csv
with open('archivo.csv') as f:#se usa para mostrar contenido csv
    reader = csv.reader(f,delimiter="$")
    for row in reader:
        print("Ap paterno: {0}, Ap materno: {1}, Nombre: {2}, Ciudad: {3} ".format(row[0],row[1],row[2],row[3]))"""
ch = 0
archivo = open('archivo.csv','r')
lectura = archivo.readline()

for i in range(6):# como extraer de un archivo csv
    lectura = archivo.readline().split(',')
    if lectura[1] == "Rivera":
        ch = ch + 1

print("el numero de personas con el nombre rivera es: ",ch)