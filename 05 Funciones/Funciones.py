#  1. Crear una función llamada imprimir_hola_mundo que imprima por
#  pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#  programa principal

saludar = "Hola Mundo"

def hola_Mundo(saludar):
    print(saludar)

hola_Mundo(saludar)

#  2. Crear una función llamada saludar_usuario(nombre) que reciba
#  como parámetro un nombre y devuelva un saludo personalizado.
#  Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
#  principal solicitando el nombre al usuario

nombre= input("Escribe tu nombre : ")

def saludar_usuario(nombre):
    print( " Hola " + nombre )

saludar_usuario(nombre)

# 3. Crear una función llamada informacion_personal(nombre, apellido,
#  edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#  [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
# dir los datos al usuario y llamar a esta función con los valores in
# gresados.

nombre= input("Escribe tu nombre : ")
apellido= input("Escribe tu apellido : ")
edad= int(input("Escribe tu edad : "))
residencia= input("Escribe tu residencia : ")


def informacion_personal(nombre,apellido,edad,residencia):
     print(f" Soy  {nombre} {apellido}, Tengo {edad} años y vivo {residencia} ")

informacion_personal(nombre,apellido,edad,residencia)

#  4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.
import math
radio= int(input("Escribe el radio : "))
pi= math.pi

def calcular_area_circulo(radio):
    area = pi * radio ** 2
    return area

print(calcular_area_circulo(radio))

def calcular_perimetro_circulo(radio):
    perimetro = (radio * 2) * pi
    return perimetro

print(calcular_perimetro_circulo(radio))

#  5. Crear una función llamada segundos_a_horas(segundos) que reciba
#  una cantidad de segundos como parámetro y devuelva la cantidad
#  de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.

segundos= float(input("Escribe los segundos : "))

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

print(segundos_a_horas(segundos))

#  6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#  número como parámetro y imprima la tabla de multiplicar de ese
#  número del 1 al 10. Pedir al usuario el número y llamar a la fun
# ción

numero= int(input("Escribe tu numero que deseas multiplicar : "))

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        # Imprimimos cada línea de la tabla
        print(f"{numero} x {i} = {resultado}")
        
tabla_multiplicar(numero)

#  7. Crear una función llamada operaciones_basicas(a, b) que reciba
#  dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.

a= int(input("Escribe tu numero  : "))
b= int(input("Escribe tu numero  : "))

def operaciones_basicas(a, b):
    sumar = a + b
    restar = a - b
    multiplicar = a * b
    dividir = a / b
    print(f"La suma de a + b es {sumar} la resta es {restar} la multiplicacion es {multiplicar} y la division es {dividir}")

operaciones_basicas(a, b)

#  8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#  peso en kilogramos y la altura en metros, y devuelva el índice de
#  masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.

peso= float(input("Escribe tu numero  : "))
altura= float(input("Escribe tu numero  : "))

def calcular_imc(peso, altura):
    imc = peso / altura ** 2
    print(f" El indice imc es {imc}")
    
calcular_imc(peso, altura)

#  9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#  una temperatura en grados Celsius y devuelva su equivalente en
#  Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#  resultado usando la función.

celsius= float(input("Escribe tu numero  : "))

def celsius_a_fahrenheit(celsius):
    grado = celsius * 1.8 + 32
    print(f"Los grados Fahrenheit son : {grado} ")
    

celsius_a_fahrenheit(celsius)

#  10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#  tres números como parámetros y devuelva el promedio de ellos.
#  Solicitar los números al usuario y mostrar el resultado usando esta
#  función.

a= int(input("Escribe tu numero  : "))
b= int(input("Escribe tu numero  : "))
c= int(input("Escribe tu numero  : "))

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio de abc es: {promedio}")

calcular_promedio(a, b, c)