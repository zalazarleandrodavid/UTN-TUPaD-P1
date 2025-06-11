import time
import random
import tracemalloc

# Algoritmo 1: Buscar el máximo manualmente
def encontrar_maximo_manual(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

# Algoritmo 2: Usar la función incorporada max()
def encontrar_maximo_con_max(lista):
    return max(lista)

# Función para medir el tiempo de ejecución
def medir_tiempo(funcion, lista):
    inicio = time.time()
    resultado = funcion(lista)
    fin = time.time()
    return resultado, fin - inicio

# Función para medir el uso de memoria
def medir_memoria(funcion, lista):
    tracemalloc.start()
    funcion(lista)
    memoria_actual, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return memoria_actual, pico

if __name__ == "__main__":
    # Crear una lista grande con números aleatorios
    lista = [random.randint(1, 10000000) for _ in range(10000000)]

    print("Buscando el número más grande en la lista...\n")

    # Medición para el algoritmo 1 (búsqueda manual)
    resultado1, tiempo1 = medir_tiempo(encontrar_maximo_manual, lista)
    memoria1_actual, memoria1_pico = medir_memoria(encontrar_maximo_manual, lista)
    print(f"Búsqueda Manual: Resultado={resultado1}, Tiempo={tiempo1} segundos, Memoria pico={memoria1_pico / 1024} KB")

    # Medición para el algoritmo 2 (usando max)
    resultado2, tiempo2 = medir_tiempo(encontrar_maximo_con_max, lista)
    memoria2_actual, memoria2_pico = medir_memoria(encontrar_maximo_con_max, lista)
    print(f"Usando max():    Resultado={resultado2}, Tiempo={tiempo2} segundos, Memoria pico={memoria2_pico / 1024} KB")

    print("\n--- Comparación de rendimiento ---")
    if tiempo2 > 0:
        print(f"La búsqueda manual tardó {tiempo1 / tiempo2} veces más que usar max().")
    else:
        print("La función max() fue extremadamente rápida (tiempo cercano a cero).")
