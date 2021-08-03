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

