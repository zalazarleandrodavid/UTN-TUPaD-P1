# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir las nuevas frutas y sus precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Pera'] = 2800

print(precios_frutas)


# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Pera'] = 2800

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.


contactos = {}

print("--- Carga de 5 contactos ---")
# Permitir al usuario cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingresa el nombre del contacto #{i+1}: ")
    numero = input(f"Ingresa el número de teléfono para {nombre}: ")
    contactos[nombre] = numero # Añade el contacto al diccionario
    print(f"Contacto '{nombre}' guardado.")

print("\n--- Consulta de números telefónicos ---")
# Pedir un nombre para consultar
nombre_buscar = input("Ingresa el nombre del contacto que deseas buscar: ")

# Mostrar el número asociado si existe
if nombre_buscar in contactos:
    print(f"El número de teléfono de {nombre_buscar} es: {contactos[nombre_buscar]}")
else:
    print(f"Lo siento, el contacto '{nombre_buscar}' no se encontró en la agenda.")

print("\n--- Fin del programa ---")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

import string


# 1. Solicitar al usuario una frase
frase = input("Por favor, ingresa una frase: ")

# 2. Preprocesar la frase para limpiar y estandarizar las palabras
# Convertir a minúsculas para tratar "La" y "la" como la misma palabra
frase_limpia = frase.lower()


for caracter_puntuacion in string.punctuation:
    frase_limpia = frase_limpia.replace(caracter_puntuacion, "")

palabras = frase_limpia.split()

# 3. Obtener las palabras únicas (usando un set)
# Al convertir una lista a un set, los elementos duplicados se eliminan automáticamente
palabras_unicas = set(palabras)

print("\n--- Palabras únicas ---")
print(palabras_unicas)

# 4. Crear un diccionario con la cantidad de veces que aparece cada palabra
frecuencia_palabras = {}
for palabra in palabras:
    # Si la palabra ya está en el diccionario, incrementa su contador
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    # Si la palabra no está, la añade con un contador de 1
    else:
        frecuencia_palabras[palabra] = 1

print("\n--- Frecuencia de cada palabra ---")
print(frecuencia_palabras)

print("\n--- Fin del programa ---")

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.


# Diccionario para almacenar los alumnos y sus notas
# La clave será el nombre del alumno y el valor será una tupla de sus notas.
alumnos_notas = {}

print("--- Ingreso de notas de 3 alumnos ---")

# Bucle para ingresar los datos de 3 alumnos
for i in range(3):
    nombre_alumno = input(f"\nIngresa el nombre del alumno #{i+1}: ")

    # Bucle para ingresar las 3 notas para el alumno actual
    notas_lista = [] # Usamos una lista temporal para recolectar las notas
    for j in range(3):
        while True: # Bucle para asegurar que la entrada es un número válido
            try:
                nota = float(input(f"Ingresa la nota #{j+1} para {nombre_alumno}: "))
                if 0 <= nota <= 10: # Opcional: validar que la nota esté en un rango razonable
                    notas_lista.append(nota)
                    break # Salir del bucle interno si la nota es válida
                else:
                    print("Por favor, ingresa una nota entre 0 y 10.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número para la nota.")

    # Convertir la lista de notas a una tupla y asignarla al alumno en el diccionario
    alumnos_notas[nombre_alumno] = tuple(notas_lista)
    print(f"Notas de {nombre_alumno} guardadas: {alumnos_notas[nombre_alumno]}")

print("\n--- Promedios de los alumnos ---")

# Iterar sobre el diccionario para calcular y mostrar el promedio de cada alumno
if alumnos_notas: # Verificar si el diccionario no está vacío
    for alumno, notas_tupla in alumnos_notas.items():
        # Calcular el promedio: suma de notas / cantidad de notas
        promedio = sum(notas_tupla) / len(notas_tupla)
        print(f"El promedio de {alumno} es: {promedio:.2f}") # Formatear a 2 decimales
else:
    print("No se ingresaron datos de alumnos.")

print("\n--- Fin del programa ---")



# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


alumnos_notas = {}

print("--- Ingreso de notas de 3 alumnos ---")

# Bucle para ingresar los datos de 3 alumnos
for i in range(3):
    nombre_alumno = input(f"\nIngresa el nombre del alumno #{i+1}: ")

    notas_lista = []
    for j in range(3):
        while True:
            try:
                nota = float(input(f"Ingresa la nota #{j+1} para {nombre_alumno}: "))
                if 0 <= nota <= 10:
                    notas_lista.append(nota)
                    break
                else:
                    print("Por favor, ingresa una nota entre 0 y 10.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número para la nota.")

    alumnos_notas[nombre_alumno] = tuple(notas_lista)
    print(f"Notas de {nombre_alumno} guardadas: {alumnos_notas[nombre_alumno]}")

print("\n--- Promedios de los alumnos ---")

# Define la nota mínima de aprobación
NOTA_MINIMA_APROBACION = 6.0 # Puedes cambiar este valor según tu criterio

alumnos_aprobados = [] # Lista para almacenar los nombres de los alumnos aprobados

if alumnos_notas:
    for alumno, notas_tupla in alumnos_notas.items():
        promedio = sum(notas_tupla) / len(notas_tupla)
        print(f"El promedio de {alumno} es: {promedio:.2f}")

        # Aquí es donde comparas para saber si aprobó
        if promedio >= NOTA_MINIMA_APROBACION:
            print(f"¡{alumno} ha APROBADO!")
            alumnos_aprobados.append(alumno) # Añade el alumno a la lista de aprobados
        else:
            print(f"{alumno} ha DESAPROBADO.")
else:
    print("No se ingresaron datos de alumnos.")

print(f"\n--- Resumen de Alumnos Aprobados (promedio >= {NOTA_MINIMA_APROBACION}) ---")
if alumnos_aprobados:
    for alumno_aprobado in alumnos_aprobados:
        print(f"- {alumno_aprobado}")
else:
    print("Ningún alumno aprobó con el criterio establecido.")


print("\n--- Fin del programa ---")

# 8) Programa básico para gestionar stock de productos

# Diccionario inicial de stock (puedes empezar con algunos productos o vacío)
stock_productos = {
    "camisa": 10,
    "pantalon": 5,
    "zapatillas": 8
}

print("--- Gestión de Stock de Productos ---")

while True:
    print("\nOpciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades / Añadir nuevo producto")
    print("3. Ver todo el stock")
    print("4. Salir")

    opcion = input("Ingresa el número de tu opción: ")

    if opcion == '1':
        # Consultar el stock de un producto
        nombre_producto = input("Ingresa el nombre del producto a consultar: ").lower() # .lower() para ser insensible a mayúsculas/minúsculas
        if nombre_producto in stock_productos:
            print(f"Stock de '{nombre_producto}': {stock_productos[nombre_producto]} unidades.")
        else:
            print(f"El producto '{nombre_producto}' no se encuentra en el stock.")

    elif opcion == '2':
        # Agregar unidades o añadir nuevo producto
        nombre_producto = input("Ingresa el nombre del producto (existente o nuevo): ").lower()
        while True:
            try:
                cantidad_a_agregar = int(input(f"¿Cuántas unidades deseas agregar a '{nombre_producto}'?: "))
                if cantidad_a_agregar >= 0: # No permitir agregar cantidades negativas
                    break
                else:
                    print("Por favor, ingresa un número positivo o cero.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero.")

        if nombre_producto in stock_productos:
            # El producto ya existe, se añaden unidades
            stock_productos[nombre_producto] += cantidad_a_agregar
            print(f"Se agregaron {cantidad_a_agregar} unidades a '{nombre_producto}'. Nuevo stock: {stock_productos[nombre_producto]}.")
        else:
            # El producto no existe, se agrega como nuevo
            stock_productos[nombre_producto] = cantidad_a_agregar
            print(f"Nuevo producto '{nombre_producto}' agregado con stock inicial de {cantidad_a_agregar} unidades.")

    elif opcion == '3':
        # Ver todo el stock
        if stock_productos:
            print("\n--- STOCK ACTUAL ---")
            for producto, stock in stock_productos.items():
                print(f"{producto.capitalize()}: {stock} unidades") # .capitalize() para que se vea mejor
            print("--------------------")
        else:
            print("El stock está vacío.")

    elif opcion == '4':
        print("Saliendo del programa. ¡Hasta luego!")
        break # Sale del bucle while True

    else:
        print("Opción no válida. Por favor, elige 1, 2, 3 o 4.")

# 9) Agenda con tuplas (día, hora) como claves y eventos como valores (VERSIÓN SIMPLE)

# Diccionario para almacenar la agenda
agenda = {}

print("--- Creación de la Agenda  ---")

# 1. Agregar eventos
# Los días y horas se ingresan directamente como números para simplificar
agenda[(27, 9)] = "Reunión con el equipo"
agenda[(27, 14)] = "Presentación de proyecto"
agenda[(28, 10)] = "Llamada con cliente Juan"
agenda[(29, 18)] = "Cena de cumpleaños"

print("\n--- Eventos agregados ---")
print(agenda)

# 2. Consultar un evento específico
dia_consulta = 27
hora_consulta = 9
clave_consulta = (dia_consulta, hora_consulta)

print(f"\n--- Consulta de evento para el día {dia_consulta} a las {hora_consulta}:00 hs ---")
if clave_consulta in agenda:
    print(f"Evento: '{agenda[clave_consulta]}'")
else:
    print("No se encontró ningún evento para esa fecha y hora.")

# 3. Consultar otro evento que no existe
dia_consulta_no_existe = 30
hora_consulta_no_existe = 11
clave_consulta_no_existe = (dia_consulta_no_existe, hora_consulta_no_existe)

print(f"\n--- Consulta de evento para el día {dia_consulta_no_existe} a las {hora_consulta_no_existe}:00 hs ---")
if clave_consulta_no_existe in agenda:
    print(f"Evento: '{agenda[clave_consulta_no_existe]}'")
else:
    print("No se encontró ningún evento para esa fecha y hora.")


# 4. Ver toda la agenda (ordenada para mejor lectura)
print("\n--- Agenda Completa (Ordenada) ---")
eventos_ordenados = sorted(agenda.items())
for (dia, hora), evento in eventos_ordenados:
    print(f"Día {dia}, {hora:02d}:00 hs: {evento}")

print("\n--- Fin del programa ---")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.


# Diccionario original: países como claves, capitales como valores
paises_capitales = {
    "Argentina": "Buenos Aires",
    "España": "Madrid",
    "Francia": "París",
    "Alemania": "Berlín",
    "Italia": "Roma"
}

print("--- Diccionario Original (Países -> Capitales) ---")
print(paises_capitales)

# Construir el nuevo diccionario invertido
# Donde las capitales son las claves y los países son los valores

capitales_paises = {} # Inicializamos un diccionario vacío para el resultado

# Iteramos sobre los elementos (clave, valor) del diccionario original
for pais, capital in paises_capitales.items():
    # Asignamos la 'capital' como la nueva clave
    # y el 'pais' como el nuevo valor
    capitales_paises[capital] = pais

print("\n--- Nuevo Diccionario (Capitales -> Países) ---")
print(capitales_paises)

print("\n--- Fin del programa ---")