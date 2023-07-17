import csv

total_registros = 0

dedicacion = { "full_time": [], "part_time": [] }
pago_dolares = { "si": [], "no": [], "parcial": []}
conformidad = {}
todos = []

with open("encuesta.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for data in csvreader:
        #Se genera listado completo
        todos.append(data)
        print("")
        
        #Cataloga por conformidad
        if (total_registros > 0):
            if (data[13] in conformidad):
                conformidad[str(data[13])].append(data)
            else:
                conformidad[str(data[13])] = []
                conformidad[str(data[13])].append(data)

        #Cataloga por dedicacion horaria
        if (data[2] == 'Full-Time'):
            dedicacion["full_time"].append(data)
        if (data[2] == 'Part-Time'):
            dedicacion["part_time"].append(data)

        #Cataloga por pago en dolares
        if (data[6] == ''):
            pago_dolares["no"].append(data)
        total_registros = total_registros + 1


print(str(total_registros)+' Registros')

print("Conformidad salario:")
keys_conformidad = conformidad.keys()
for key in keys_conformidad:
    print("- "+str(key)+': '+str( len(conformidad[key]) / (total_registros/100) ) + "%")