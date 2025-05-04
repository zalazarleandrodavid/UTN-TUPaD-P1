# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.

my_lista = list(range(1,101))
print(my_lista)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el 
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el 
# indexing con números negativos! 

element_list = ["uva", 12, 24, "milanesa", True]

interesante = element_list[-2]
print(interesante)

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por 
# ejemplo: 
# lista_vacia = [] 

lista_vacia = []

lista_vacia.append("manzana")
lista_vacia.append(25)
lista_vacia.append(True)


print(lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
# respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra 
# en los videos o bien investigar cómo funciona el indexing con números negativos! 
# animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]

animales[1]= "loro"
animales[-1]= "oso"

print(animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. 

# numeros=[8,15,3,22,7]
# numeros.remove(max(numeros))
# print(numeros)

# Este programa busca en el array de numeros, el numero mayor de todos ellos y lo remueve, dejando todo los demas
# Despues con la funcion print se muestra el numero resultado.

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
# pantalla los dos primeros.

my_lista = list(range(10,31,5))
print(my_lista)

