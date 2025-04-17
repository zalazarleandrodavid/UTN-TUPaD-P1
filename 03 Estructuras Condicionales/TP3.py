#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.


print("Colocar edad")
edad = int(input())  # Leemos la data del usuario

if edad >= 18:
    print("Eres Mayor de edad")
else:
    print("Eres menor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

print("Colocar tu nota")

nota = float(input()) # Leemos la data del usuario

if nota >= 6:
    print("Estas aprobado")
else:
    print("Estas desaprobado")


# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

print("Ingresar un numero par")

num = int(input()) # Leemos la data del usuario

if num % 2 == 0: # Sacamos el modulo del numero indicado por el usuario
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.


print("Colocar edad")
edad = int(input())  # Leemos la data del usuario

if edad < 12: # Generamos las condiciones para su ejecucion
    print("Eres un niño")
elif edad >= 12 and edad < 18:
    print("Eres un adolecente")
elif edad >= 18 and edad < 30:
    print("Eres un adulto joven")
elif edad >= 30:
    print("Eres un adulto")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

print("Por favor ingresar su contraseña")
pasw = str(input())  # Leemos la data del usuario

if len(pasw) >= 8 and len(pasw) <= 14:# Se usa la funcion len para poder contar y comparar los caracteres
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100000) for i in range(500)] # Gera numeros aleatorios

media=mean(numeros_aleatorios) # Genera la media de los numeros aleatorios
print(media)
mediana=median(numeros_aleatorios) # Genera la mediana de los numeros aleatorios
print(mediana)
moda= mode(numeros_aleatorios) # Genera la moda de los numeros aleatorios
print(moda)

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

print("Por una palabra o frase")
pal = str(input()) # Leemos la data del usuario
vocales= "AEIOUaeiou" # Asiganamos valor a la variable a comparar

if pal:

    pal2= pal[-1] # Restamos uno para poder comparar la ultima letra

    es_vocal = (pal2 == vocales[0] or pal2 == vocales[1] or     # generamos comparacion atravez de la posicion
                    pal2 == vocales[2] or pal2 == vocales[3] or
                    pal2 == vocales[4] or pal2 == vocales[5] or
                    pal2 == vocales[6] or pal2 == vocales[7] or
                    pal2 == vocales[8] or pal2 == vocales[9])

if es_vocal:            # Si es_vocal es verdadera se aplica lo solicitado
    salida= pal + "!"
    print(salida)
else:
    print(pal)


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.


print("Escribe tu nombre")
name = str(input())

print("Escribir la Opcion deseada")
print("Escribe 1 Si quiere su nombre en mayúsculas")
print("Escribe 2 Si quiere su nombre en minúsculas")
print("Escribe 3 Si quiere su nombre con la primera letra mayúscula")

num= int(input())

if num == 1:
    mayus= name.upper()
    print(mayus)
elif num == 2:
    minus= name.lower()
    print(minus)

elif num == 3:
    title= name.title()
    print(title)


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).


print("Describa la magnitud del terremoto que presencio")

print("Menor que 3: Muy leve (imperceptible)")
print("Mayor o igual que 3  y menor que 4: Leve (ligeramente perceptible)")
print("Mayor o igual que 4  y menor que 5: Moderado (sentido por personas, pero generalmente no causa daños). ")
print("Mayor o igual que 5  y menor que 6: Fuerte (puede causar daños en estructuras débiles).")
print("Mayor o igual que 6  y menor que 7: Muy Fuerte (puede causar daños significativos).")
print("Mayor o igual que 7: Extremo (puede causar graves daños a gran escala).")

num= float(input("Por favor indicar el valor numerico"))

if num <=3:
    print("El terremoto que describe esta considerado como muy leve")

elif num >= 3 and num <4:
    print("El terremoto que describe esta considerado como leve ")

elif num >= 4 and num <5:
    print("El terremoto que describe esta considerado como moderado ")

elif num >= 5 and num <6:
    print("El terremoto que describe esta considerado como fuerte ")

elif num >= 6 and num <7:
    print("El terremoto que describe esta considerado como muy fuerte ")

elif num >= 7:
    print("El terremoto que describe esta considerado como extremo ")

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

print("Estaciones del año")

print("Indique en que hemisferio se encuentra")
print("1 Si esta en el hemisferio Sur")
print("2 Si esta en el hemisferio Norte")

hemis= int(input("Indicar hemisferio del planeta te encuentras ")) # Hemisferio a seleccionar

enero= 1
febrero = 2
marzo = 3
abril = 4
mayo = 5
junio = 6
julio = 7
agosto = 8
septiembre = 9
octubre = 10
noviembre = 11
diciembre = 12

if hemis == 1 or hemis == 2: # Comprueba si el numero ingresado es correcto
    
    mes= int(input("Indicar el mes del año : "))
    dia= int(input("Indicar el dia del mes : "))

else:
    print("Hemisferio inválido")


if hemis == 1: # Hemisferio Sur
    if (mes == diciembre and dia >= 21) or mes == enero or mes == febrero or (mes == marzo and dia <= 20):
        print("Verano")
    elif (mes == marzo and dia >= 21) or mes == abril or mes == mayo or (mes == junio and dia <= 20):
        print("Otoño")
    elif (mes == junio and dia >= 21) or mes == julio or mes == agosto or (mes == septiembre and dia <= 22):
        print("Invierno")
    elif (mes == septiembre and dia >= 23) or mes == octubre or mes == noviembre or (mes == diciembre and dia <= 20):
        print("Primavera")
    else:
        print("Fecha inválida")
elif hemis == 2:  # Hemisferio Norte
    if (mes == marzo and dia >= 20) or mes == abril or mes == mayo or (mes == junio and dia <= 20):
        print("Primavera")
    elif (mes == junio and dia >= 21) or mes == julio or mes == agosto or (mes == septiembre and dia <= 22):
        print("Verano")
    elif (mes == septiembre and dia >= 23) or mes == octubre or mes == noviembre or (mes == diciembre and dia <= 21):
        print("Otoño")
    elif (mes == diciembre and dia >= 22) or mes == enero or mes == febrero or (mes == marzo and dia <= 19):
        print("Invierno")
    else:
        print("Fecha inválida")