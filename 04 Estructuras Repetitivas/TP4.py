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