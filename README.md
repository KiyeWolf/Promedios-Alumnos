Promedios de Alumnos

**Este programa ayuda a los profesores a organizar la planilla de alumnos con sus respectivas notas. Permite ingresar nombres, apellidos y notas de los estudiantes, y luego calcula y muestra su condición final, promedio y el mejor estudiante de la camada. Además, genera un archivo CSV con los datos ordenados y un gráfico de barras para visualizar mejor los promedios.**
---
**Funcionalidades**

➔ Ingreso de nombres, apellidos y dos notas por alumno.

➔ Cálculo del promedio de cada estudiante.

➔ Determinación de la condición final según el promedio:

  Promociona (Ambas notas ≥ 7)
  
  Recuperatorio opcional (Una nota ≥ 7 y otra ≥ 4)
  
  Debe rendir final (Ambas notas entre 4 y 6)
  
  Debe recuperar (Una nota < 4)
  
  Reprueba (Ambas notas < 4)

➔ Identificación del mejor promedio.

➔ Guardado de los datos en un archivo CSV ordenado alfabéticamente.

➔ Generación de un gráfico de barras con los promedios de los alumnos.

---
**¿Cómo Utilizarlo?**

1.  El programa principal se encuentra en el archivo "Profesor_examenes.py", Puedes clonar el repositorio o simplemente bajar este archivo.
2.  Al abrirlo el programa explica brevemente los datos a solicitar de los alumnos. Primero necesitando del apellido, luego el nombre y las dos notas. Para finalizar la carga de alumnos se debe ingresar un "0" en la categoría Apellido.
3.  Una vez finalizada la carga, se solicita el nombre para el documento CSV donde se cargarán los alumnos; con sus notas, su promedio calculado y la condición final de cada uno, ordenado alfabéticamente por Apellido.
4.  Despues de esto el CSV automáticamente se guardará en la misma ubicación desde donde se está abriendo el programa, con el nombre seleccionado.
5.  Se mostrará un Listado de los alumnos, mostrando su condición final; Más adelante, se muestra el alumno con mejor promedio.
6.  Finalmente se solicita el nombre del grafico de barras. Una vez ingresado este se guardará también en la misma ubicación desde donde se abre el programa y se mostrará una vista previa del mismo.

**Imágen de Ejemplo**

![Promedio_Alumnos](https://github.com/user-attachments/assets/ef472043-c301-4b5e-a847-51f57970dc88)

---
**Tecnologías utilizadas**

Python

Pandas para manejo de datos.

Matplotlib para gráficos.

CSV para almacenamiento de datos.

---

Este es uno de mis primeros proyectos en Python, creado con el objetivo de aprender a manejar archivos, listas, Pandas y visualización de datos.

⭐ ¡Si te resulta útil, dale una estrella! ⭐
