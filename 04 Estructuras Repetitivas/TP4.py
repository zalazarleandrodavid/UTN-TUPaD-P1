# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
i=0
for i in range(0, 101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene.

num = int(input("Indicar tu numero"))
digi = str(num)
cantidad= len(digi)
print(" La cantidad de digitos de tu numero es: ", cantidad)

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores.

num1= int(input("Indicar el mayor de tus numeros"))
num2= int(input("Indicar el menor de tus numeros"))

cont=0

for i in range(num1 +1, num2):
    cont = cont+ i
    
suma= str(cont)   
print(" La suma de dos numeros enteros ingresados es ",suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0.
cont= 0 
num= 1
while num != 0: 
    num= int(input("Colocar tu numero"))
    
    cont = cont + num
    print(cont)
    
# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
print(" Juega a encuentra el numero")

cont= 0 
num= 0
numero_secreto = random.randint(0, 9)

while numero_secreto > 0 and numero_secreto <=9: 
    num= int(input("Colocar tu numero de entre 0 y 9"))
    cont = cont + 1
  
    if num < numero_secreto:
        print(" Tu numero es menor")
    elif num > numero_secreto:
        print(" Tu numero es mayor")
    elif num == numero_secreto:
        print(" Felicidades encontraste tu numero y tus cantidad de intentos fueron:",cont)    
        
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

i = 100

while i >= 0:
    print(i)
    i = i - 2
    
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 


num1= 0
num2= int(input("Indicar el menor de tus numeros"))

cont=0

for i in range(num1 +1, num2):
    cont = cont+ i
    
suma= str(cont)   
print(" La suma de todos los números comprendidos entre 0 y un numero positivo es ",suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 


print(f"Por favor, ingrese la cantidad de números enteros a trabajar:")
cantidad_numeros = int(input()) # Cantidad de numeros a ingresar

pares = 0
impares = 0
positivos = 0
negativos = 0

if cantidad_numeros > 100:
    print("Error: no puede colocar más de 100 números")
else:
    for i in range(cantidad_numeros): # Ciclo para ingreso de numeros segun el usuario
        print("Ingrese el número :", i + 1)
        numero = int(input())
        
        if numero % 2 == 0: # Comprobacion de pares e impares
            pares = pares + 1
        else:
            impares = pares + 1

        if numero > 0:  # Comprobacion de positivos y negativos
            positivos = positivos + 1
        elif numero < 0:
            negativos= negativos + 1

    print(" Analisis de numeros ")
    print("Cantidad de números pares:", pares)
    print("Cantidad de números impares:", impares)
    print("Cantidad de números positivos: ", positivos)
    print("Cantidad de números negativos:", negativos)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).


print(f"Por favor, ingrese la cantidad de números enteros a trabajar:")
cantidad_numeros = int(input()) # Cantidad de numeros a ingresar

suma = 0
media = 0

if cantidad_numeros > 100:
    print("Error: no puede colocar más de 100 números")
else:
    for i in range(cantidad_numeros): # Ciclo para ingreso de numeros segun el usuario
        print("Ingrese el número :", i + 1)
        numero = int(input())
        suma =  suma + numero       # Se usa acomula y se va su mando por cada iteracion 
    
    media = suma / cantidad_numeros # Calcular la media
    print(media)
    
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

num = int(input("Introducir su numero: "))
num2 = str(num) # convierte la cadena en string
num_invertido = ""

for i in reversed(num2): # reversed invierte la cadena
    num_invertido = num_invertido + i

print("El número invertido es:", num_invertido)