import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

total_registros = 0

dedicacion = { "full_time": [], "part_time": [] }
pago_dolares = { "si": [], "no": [], "parcial": []}
conformidad = {}
beneficios = {}
todos = []

with open("encuesta.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for data in csvreader:
        #Se genera listado completo
        todos.append(data)
        print(data)
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

            #Mencion a beneficios
            if (data[15] != ''):
                reg_beneficios = data[14].split(',')
                for beneficio in reg_beneficios:
                    if (beneficio in beneficios):
                        beneficios[beneficio] = beneficios[beneficio] + 1
                    else:
                        beneficios[beneficio] = 1

        total_registros = total_registros + 1


print(str(total_registros)+' Registros')

grafica_conformidad = []
labels_grafica_conformidad = []
print("Conformidad salario:")
keys_conformidad = conformidad.keys()
for key in keys_conformidad:
    grafica_conformidad.append( len(conformidad[key]) / (total_registros/100) )
    labels_grafica_conformidad.append( key )
    print("- "+str(key)+': '+str( len(conformidad[key]) / (total_registros/100) ) + "%")


explode = (0.1, 0, 0, 0)  

fig1, ax1 = plt.subplots()
#Creamos el grafico, añadiendo los valores
ax1.pie(grafica_conformidad, explode=explode, labels=labels_grafica_conformidad, autopct='%1.1f%%',
        shadow=True, startangle=90)
#señalamos la forma, en este caso 'equal' es para dar forma circular
ax1.axis('equal')
plt.title("Conformidad POr Sueldo")
plt.legend()
plt.savefig('conformidad_sueldos.png')
plt.show()

print("Menciones Beneficios")
key_beneficios = beneficios.keys()
for key in key_beneficios:
    print("- "+str(key)+': '+ str(beneficios[key]))
