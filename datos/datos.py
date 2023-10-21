miarchivo = open ("datos.csv","w")
miarchivo.write("nombre"+",")
miarchivo.write("apellido"+",")
miarchivo.write("sexo"+",")
miarchivo.write("edad"+"\n")

cantidad = int(input("digite el numero de registros"))

for i in range(cantidad):
    nombre = input("digite el nombre posicion"+ str(i) + ",")
    apellido = input("digite el apellido posicion"+ str(i) + ",")
    sexo = input("digite el sexo posicion"+ str(i) + ",")
    edad = input("digite el edad posicion"+ str(i) + ",")

    miarchivo.write(nombre + ",")
    miarchivo.write(apellido + ",")
    miarchivo.write(sexo + ",")
    miarchivo.write(edad + "\n")