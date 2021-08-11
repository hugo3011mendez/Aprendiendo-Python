# -------------------------- CONDICIONALES -----------------------------------------------------

if 2 > 1: # Así se hace un if, usando identación
    print("2 es mayor que 1")
else:
    print("2 es menor que 1")


print("Programa de evaluación de notas de alumnos")

nota_alumno = input("Escriba su nota : ") # Así se guarda un dato en una variable escribiendo por pantalla
# Función con condicional :
def evaluacion(nota):
    if nota < 5:
        return "Evaluación Suspensa"
    else:
        return "Evaluación Aprobada"

print(evaluacion(int(nota_alumno)))