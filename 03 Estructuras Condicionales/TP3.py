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

nota = float(input())

if nota >= 6:
    print("Estas aprobado")
else:
    print("Estas desaprobado")