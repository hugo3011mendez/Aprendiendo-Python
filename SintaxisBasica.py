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

print(miLista.index("Hugo")) # Así puedo saber el índice de un elemento en concreto
# Si existe el mismo elemento en más de una posición, se mostrará el índice del primer elemento
print("Jake" in miLista) # Devuelve True o False según el elemento indicado se encuentra en el array o no

miLista2 = [1, 2]
miLista3 = miLista + miLista2 # Se pueden sumar listas así de fácil


# TUPLAS :
# Son estructuras parecidas a las listas, pero con restricciones
# Una tupla es una lista inmutable, en ella no podemos añadir, eliminar o mover elementos
# Sí permiten extraer porciones, pero el resultado de ello será otra tupla nueva
# Permiten comprobar si un elemento se encuentra en una tupla
# Las tuplas son más rápidas de acceder que las listas, ocupan menos espacio, pueden formatear strings y utilizarse como claves en un diccionario

miTupla=("Juan", 2, True) # Así es la sintaxis de una tupla entre paréntesis y separando elementos con una coma, puede contener cualquier tipo de variable
# Una tupla de 1 elemento se define como tupla unitaria
print(miTupla[0]) # Así puedo acceder a un elemento de la tupla

miLista = list(miTupla) # Puedo guardar la tupla como una lista de esta manera, con la función list()
miTupla = tuple(miLista2) # Y así haría la operación inversa, cambiar a tupla una lista

print("Juan" in miTupla) # Así puedo comprobar si algo se encuentra en una tupla
print(miTupla.count("Juan")) # Así se muestra las veces que el elemento se encuentra en la tupla
print(len(miTupla)) # Longitud de la tupla, muestra cuántos elementos hay

# Desempaquetado de tupla :
nombre = "Hugo"
apellido ="Méndez"
nombre, apellido = miTupla # Así también puedo asignarle valores a una tupla


# DICCIONARIOS :
# Es una estructura en la que al almacenar un dato se realiza en forma de clave -> valor
# Los tipos que se pueden guardar en un diccionario pueden ser hasta tuplas, listas u otro diccionario
# Los elementos almacenados no están ordenados, es decir, no importa si los almacenamos primero o después
# Las claves y los valores pueden ser de cualquier tipo de variable, hasta una lista o una tupla

# Los elementos de un diccionario van entre llaves
miDiccionario = {"Alemania":"Berlín", "España":"Madrid", "Finlandia":"Helsinki", "UK":"Londres", "Argentina":"Buenos Aires"} # Así es la sintaxis
miDiccionario["USA"] = "Washington D.C" # Así añado un nuevo par clave -> valor
miDiccionario["USA"] = "Chicago" # Ahora actualizaría el valor de la clave "USA" en vez de añadir un par clave -> valor nuevo
del miDiccionario["USA"] # Así elimino un par del diccionario

print("Todo el diccionario : " + str(miDiccionario)) # Muestro todo el diccionario
print("La capital de España es " + str(miDiccionario["España"])) # Muestro un valor refiriéndome a su clave
print("Las claves son : " + str(miDiccionario.keys())) # Muestro en pantalla las claves de los pares del diccionario
print("Los valores son : " + str(miDiccionario.values())) # Muestro en pantalla los valores de los pares del diccionario
print("Longitud del diccionario : " + str(len(miDiccionario))) # Muestro la longitud del diccionario contando los pares que contiene