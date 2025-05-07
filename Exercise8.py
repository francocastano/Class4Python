"""
Ejercicio 8

Calcular el promedio de las calificaciones de los estudiantes.
Los estudiantes serán cargados por el usuario en un diccionario "Nombre: Calificación".

Para ello pídale que primero ingrese la CANTIDAD de estudiantes que se ingresarán,
para luego ingresar el NOMBRE y la CALIFICACIÓN de cada uno esa cantidad de veces.

Una vez terminado este proceso, que se calcule el promedio y se muestre por pantalla.

students = {}
"""


def prom_student(students:dict) -> float:
    amount_of_student = int(input("cuantos estudiantes son"))
    input("ingrese su nombre")
    int(input("ingrese su calificacion"))

def get_grades():
    number_student:int = int(input("ingrese la cantidad de estudiantes: "))
    grades = {}
    for i in range(number_student):
        message = f"ingrese el nombre del estudiante {i+1}"
        name = input(message)
        message2 = f"ingresa la nota de estudiante {i+1}"
        grades[name] = float(input(message2))
    return grades

def calculate_grades_average(grades:dict) -> float:
    acum_grades:int = 0
    for k in grades.values():
        acum_grades = acum_grades + k
    average_grades = acum_grades / len(grades)
    return average_grades

course1 = get_grades()
average_grades = calculate_grades_average(course1)

print(average_grades)