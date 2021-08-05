print("Hello World") # Con print() se muestra info por pantalla
print("Hola"); print("Adiós") # Si escribo ';' se tomará como dos instrucciones en líneas diferentes

mi_nombre="Hugo" # Así se define una variable
print("Hola, mi nombre es " + mi_nombre) # Y así se usa una variable con print

frase="Mi nombre es \
Hugo" # Con la barra invertida '\' puedo seguir escribiendo el dato una línea más abajo
print(frase)

# Python trabaja con identación, por lo que lo que separa los bloques de código (un condicional de un bucle por ejemplo) es la identación
a=0
for i in range(5):
    a+=1
    print(a)
# Y para salir del bucle sólo se tiene que borrar el tabulador de la nueva línea donde se vaya a escribir

print("5 elevado a 2 es " + str(5**2)) # Para hacer potencias de un número, basta con realizar esta expresión
# Y para poder pasar cualquier tipo de dato a String, se puede meter dentro de la función str()

print(str(9//2)) # Con '//' se hace una división entera, es decir : El resultado siempre va a dar un número entero, el que más se aproxime al resultado real con decimales

print(type(frase)) # Con la función type() se puede saber el tipo de una variable

frase = """Hola esta es la 1
esta es la 2
esta es la 3"""
print(frase) # Con un string con 3 comillas se puede escribir en diferentes líneas y se guarda tal cual


# CONDICIONALES :

if 2 > 1: # Así se hace un if, usando identación
    print("2 es mayor que 1")
else:
    print("1 es mayor que 2")


# FUNCIONES :
# Así defino una función, después con identación establezco todas las instrucciones que quiero que tenga
def primeraFuncion():
    print("Esta es mi primera función")

primeraFuncion() # Así llamo a la función

# Función con parámetros
def suma(num1, num2): # No hace falta ni especificar de qué tipo son los parámetros
    print(str(num1 + num2))
suma(4,5)

# Función que devuelve un valor
def sumaReturn(num1, num2):
    return num1 + num2 # Tampoco hace falta especificar el tipo de valor que se devuelve
print(sumaReturn(3,2)) # Y se puede llamar sin problemas a la función


# ARRAYS :

miLista = ["Hugo", "Jake", "Patri"] # Se puede hacer una lista con cualquier tipo de variable
# Si añadiera un "*3" por ejemplo después de los elementos del array, se repetirían 3 veces

print(miLista[:]) # Así se muestran todos los elementos tal cual, con comas, comillas y entre corchetes
print(miLista[0]) # Así se puede acceder a un elemento del array en concreto por su índice
print(miLista[-1]) # Si pongo el número del índice en negativo empieza a contar elementos desde el último hacia atrás, así mostraría el último elemento
print(miLista[0:2]) # Así accedo a un rango de elementos, el 1er número del rango está incluído y el 2o elemento del rango está excluído

miLista.append("Fer") # Añado un nuevo elemento al final del array
miLista.insert(1, "Caín") # Inserto un nuevo elemento en el índice correspondiente al primer parámetro
miLista.extend(["Andrea", "Sara"]) # Añado al final los elementos contenidos en el array que está como parámetro
miLista.remove("Sara") # Elimino el elemento indicado del array
miLista.remove(5) # Elimino el elemento del índice indicado del array

print(miLista.index("Hugo")) # Así puedo saber el índice de un elemento en concreto
# Si existe el mismo elemento en más de una posición, se mostrará el índice del primer elemento
print("Jake" in miLista) # Devuelve True o False según el elemento indicado se encuentra en el array o no

miLista2 = [1, 2]
miLista3 = miLista + miLista2 # Se pueden sumar listas así de fácil