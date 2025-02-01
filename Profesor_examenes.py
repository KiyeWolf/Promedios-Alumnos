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
  
def Solicitar_string (texto):
    while True:
        nombre = input(f"Ingrese el {texto}: ")
        if nombre.isalpha()==True and len(nombre)>2:
            return nombre  
            break  
        else:
            print("Por favor ingrese mas de dos carácteres alfabeticos")


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
alumnoparcial = input("Ingrese el Apellido: ")
#valido el apellido
while(alumnoparcial!="0"):
    #VALIDO EL NOMBRE
    if len(alumnoparcial)>2:
        if alumnoparcial.isalpha() == True:
            alumnos_apellidos.append(alumnoparcial.capitalize()) 
            alumnos_nombres.append((Solicitar_string("Nombre")).capitalize()) #Pide el nombre y ademas y coloca mayuscula
            nota = Validacion_notas(1)
            nota1.append(nota)
            nota = Validacion_notas(2)
            nota2.append(nota)
            print("Alumno registrado, ingrese otro.")
        else:
            print("Por favor solo introduzca carácteres alfabéticos")    
    else:
        print("Ingrese mas de dos caracteres por favor.")
    alumnoparcial = input("Ingrese el Apellido: ")
#En este momento se obtiene la condicion del alumno
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
    print("Los datos se guardaron en el csv correctamente.")
datos_graficos_x = []
datos_graficos_y = []
muestra = []
for i in range(len(alumnos)):
    muestra = alumnos[i]
    print(f"El alumno {muestra[0]},{muestra[1]} Tiene de Condicion: {muestra[-1]}")
    datos_graficos_x.append(f"{muestra[1]} {muestra[0]}")
    datos_graficos_y.append(muestra[-2])

print(f"El Alumno con mejor promedio fue {alumno_con_mejor_promedio}, y su promedio fue {mejor_promedio}")

#Esta parte crea el grafico de barras
plt.figure(figsize=(6,3))
plt.bar(datos_graficos_x, datos_graficos_y, edgecolor='black', color=["brown","blue","gray","red","yellow"])
plt.title("Promedio de los alumnos")
plt.xlabel("Alumnos")
plt.ylabel("Promedios")
#Se agrego rotacion para mejor lectura
plt.xticks(rotation=15)
plt.savefig("Promedios_Alumnos.jpg")
plt.show()