#Un profesor desea obtener los promedios de su camada de estudiantes.
#Por cada alumno ingresa, Nombre y apellido (por separado) y Dos notas por alumno.
#Se desea mostrar en un archivo csv, por separado y ordenado por apellido y Nombre, Los alumnos. Cada uno con sus notas y su promedio.

#Además se desea obtener el alumno con mejor promedio o los alumnos con mejor promedio.
#Indicar que alumnos deberán recuperar algun examen. Nota menor que 4.
#Indicar que alumnos deben rendir un final. Nota entre 4 y 6.
#Indicar que alumnos promocionaron la materia.
import pandas as pd
import csv
import matplotlib.pyplot as plt

def Validacion_notas(num):
    while True:
        nota = input(f"Ingrese Nota {num}: ")
        try:
         nota = int(nota)
         if(nota<1 or nota>10):
             print("Nota invalida. Ingrese de nuevo.")
         else:
             return nota
        except:
            print("La nota debe ser un numero entre 1 y 10.")
            
def Obtener_condicion(nota1,nota2):
    if nota1 >= 7 and nota2 >= 7:
        condicion = "PROMOCIONA"
    elif (nota1>=7 and nota2>=4) or (nota1>=4 and nota2>=7):
        condicion = "RECUPERATORIO OPCIONAL"
    elif nota1 >= 4 and nota2 >= 4:
        condicion = "FINAL"
    elif nota1 >= 4 or nota2 >= 4:
        condicion = "DEBE RECUPERAR"
    else:
        condicion = "REPRUEBA"    
    return condicion    
    

mejor_promedio = 0
alumno_con_mejor_promedio = ""

alumnos_nombres = []
alumnos_apellidos = []
alumnos = []
nota1 = []
nota2 = []
promedio = []
alumnoparcial = ""
print("Hola, bienvenido Profesor. Porfavor Siga las indicaciones.\n Las notas se comprenden de 1 a 10 o 0 para indicar que se ausentó.\n Ingrese apellido del alumno o 0 para finalizar:")
alumnoparcial = input("Apellido: ")
while(alumnoparcial!="0"):
    alumnos_apellidos.append(alumnoparcial)
    alumnos_nombres.append(input("Ingrese Nombre: "))
    nota = Validacion_notas(1)
    nota1.append(nota)
    nota = Validacion_notas(2)
    nota2.append(nota)
    print("Alumno registrado, ingrese otro.")
    alumnoparcial = input("Apellido: ")

for i in range(len(alumnos_apellidos)):
    promedio = (nota1[i] + nota2[i]) / 2
    if (i == 0 or mejor_promedio < promedio):
        mejor_promedio = float(promedio)
        alumno_con_mejor_promedio = f"{alumnos_apellidos[i]}, {alumnos_nombres[i]}"
    condicion = Obtener_condicion(int(nota1[i]),int(nota2[i]))
    alumnos.append([alumnos_apellidos[i], alumnos_nombres[i], nota1[i], nota2[i], promedio, condicion])
alumnos.sort()

    


with open("Alumnos.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["Apellido","Nombre","Nota 1","Nota 2","Promedio","Condicion"])
    writer.writerows(alumnos)
    print("Los datos se guardaron el csv correctamente.")
datos_graficos_x = []
datos_graficos_y = []
muestra = []
for i in range(len(alumnos)):
    muestra = alumnos[i]
    print(f"El alumno {muestra[0]},{muestra[1]} Tiene de Condicion: {muestra[-1]}")
    datos_graficos_x.append(f"{muestra[1]} {muestra[0]}")
    datos_graficos_y.append(muestra[-2])

print(f"El Alumno con mejor promedio fue {alumno_con_mejor_promedio}, y su promedio fue {mejor_promedio}")


plt.figure(figsize=(6,3))
plt.bar(datos_graficos_x, datos_graficos_y, edgecolor='red')
plt.title("Promedio de los alumnos")
plt.xlabel("Alumnos")
plt.ylabel("Promedios")
plt.savefig("Promedios_Alumnos.jpg")
plt.show()