import csv #REALIZAR LA ESCRITURA DE AECHIVOS CSV
personas = [
    ['Palacios','Rivas','Adan','CDMX'],
    ['Palacios','Rivas','Adan','CDMX'],
    ['Palacios','Rivas','Adan','CDMX']
]

with open('save.csv', 'w',newline='') as file:
    writer = csv.writer(file,delimiter=";")
    writer.writerows(personas)

