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

    
    
