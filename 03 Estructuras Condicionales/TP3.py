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