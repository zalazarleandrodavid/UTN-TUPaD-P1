#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 


print("Colocar edad")
edad = int(input())  # Leemos la data del usuario

if edad >= 18:
    print("Eres Mayor de edad")
else:
    print("Eres menor de edad")