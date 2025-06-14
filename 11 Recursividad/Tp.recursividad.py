# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario 

def factorial_recursivo(numero):
    """
    Calcula el factorial de un número entero no negativo de forma recursiva.

    Args:
        numero (int): El número del cual se quiere calcular el factorial.
                      Debe ser un entero no negativo.

    Returns:
        int: El factorial del número.
             Retorna 1 si el número es 0.
             Retorna None si el número es negativo (manejo de error básico).
    """
    # CASO BASE: Si el número es 0, el factorial es 1.
    if numero == 0:
        return 1
    # CASO ESPECIAL: Si el número es negativo, el factorial no está definido.
    elif numero < 0:
        print("El factorial no está definido para números negativos.")
        return None
    # PASO RECURSIVO: Si el número es mayor que 0,
    else:
        return numero * factorial_recursivo(numero - 1)


def calcular_y_mostrar_factoriales():
    """
    Pide al usuario un número y luego calcula y muestra
    el factorial de cada entero desde 1 hasta ese número.
    """
    while True: # Bucle para asegurar que el usuario ingrese un número válido
        try:
            num = int(input("Ingresa un número entero positivo : "))
            if num < 1:
                print("Por favor, ingresa un número entero positivo (mayor o igual a 1).")
            else:
                break # Salimos del bucle si el número es válido
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

    print(f"\nCalculando factoriales desde 1 hasta {num}:\n")

    # Iteramos desde 1 hasta el número ingresado por el usuario (inclusive)
    for i in range(1, num + 1):
        resultado_factorial = factorial_recursivo(i)
        if resultado_factorial is not None:
            print(f"El factorial de {i}! es: {resultado_factorial}")
        else:
            print(f"No se pudo calcular el factorial de {i}.")

# Llama a la función principal para que todo el proceso inicie
# Esta línea estaba comentada, ¡ahora está activa!
calcular_y_mostrar_factoriales()

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique. 

def fibonacci_recursivo(posicion):
    """
    Calcula el valor de la serie de Fibonacci en la posición indicada
    de forma recursiva.

    Args:
        posicion (int): La posición en la serie de Fibonacci (debe ser un entero no negativo).

    Returns:
        int: El valor de Fibonacci en esa posición.
             Retorna None si la posición es negativa.
    """
    # Caso base 1: Si la posición es 0, el valor de Fibonacci es 0.
    if posicion == 0:
        return 0
    # Caso base 2: Si la posición es 1, el valor de Fibonacci es 1.
    elif posicion == 1:
        return 1
    # Manejo de error: Si la posición es negativa, la serie de Fibonacci no está definida.
    elif posicion < 0:
        print("La posición no puede ser un número negativo para la serie de Fibonacci.")
        return None
    # Paso recursivo: Para cualquier otra posición 'n', el valor es la suma de
    # los valores de Fibonacci en las posiciones (n-1) y (n-2).
    else:
        # Aquí la función se llama a sí misma dos veces, con 'posicion - 1' y 'posicion - 2'.
        return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)
    
    # Parte 2: Mostrar la serie completa hasta la posición especificada por el usuario

def mostrar_serie_fibonacci_completa():
    """
    Pide al usuario una posición y luego muestra la serie de Fibonacci
    completa hasta esa posición.
    """
    while True: # Bucle para asegurar que el usuario ingrese un número válido
        try:
            num = int(input("Ingresa la posición de Fibonacci : "))
            if num < 0:
                print("Por favor, ingresa una posición no negativa.")
            else:
                break # Salimos del bucle si la posición es válida
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

    print(f"\nSerie de Fibonacci hasta la posición {num}:\n")
    print("Posición | Valor")
    print("-------- | ------")

    # Iteramos desde la posición 0 hasta la posición límite (inclusive)
    for i in range(num + 1): # range(n) va de 0 a n-1, por eso sumamos 1 para incluir el límite
        valor_fib = fibonacci_recursivo(i)
        if valor_fib is not None: # Si el valor no es None (manejo de error)
            print(f"   {i:<5} | {valor_fib}") # Formato para alinear los números
        else:
            print(f"Error al calcular Fibonacci en posición {i}.") # En caso de que fibonacci_recursivo retorne None

# Ejecutamos la función principal para mostrar la serie
mostrar_serie_fibonacci_completa()

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general. 

def potencia_recursiva(base, exponente):
    """
    Calcula la potencia de un número base elevado a un exponente de forma recursiva.

    Args:
        base (int/float): El número base.
        exponente (int): El exponente (debe ser un entero no negativo para esta implementación simple).

    Returns:
        int/float: El resultado de la base elevada al exponente.
                   Retorna None si el exponente es negativo (manejo de error básico para este ejemplo).
    """
    # Caso base 1: Cualquier número elevado a la potencia de 0 es 1.
    # Esta es la condición que detiene la recursión cuando el exponente llega a 0.
    if exponente == 0:
        return 1
    # Caso especial: Si el exponente es negativo, no lo manejamos con esta fórmula recursiva simple.
    # Un exponente negativo significa 1 / (base^|exponente|).
    elif exponente < 0:
        print("Esta función recursiva simple no maneja exponentes negativos.")
        print("Para un exponente negativo 'm', el resultado sería 1 / (base ** abs(m)).")
        return None
    # Paso recursivo: Si el exponente es mayor que 0, aplicamos la fórmula n^m = n * n^(m-1).
    else:
        # Aquí la función se llama a sí misma con el exponente decrementado.
        return base * potencia_recursiva(base, exponente - 1)
    
    # Parte 2: Probar la función en un algoritmo general

def probar_calculo_potencia():
    """
    Pide al usuario una base y un exponente, y luego calcula y muestra
    la potencia utilizando la función recursiva.
    """
    # Pedir la base
    while True:
        try:
            base = float(input("Ingresa el número base (puede ser decimal): "))
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número para la base.")

    # Pedir el exponente
    while True:
        try:
            exponente = int(input("Ingresa el exponente (debe ser un número entero no negativo): "))
            if exponente < 0:
                print("Por favor, ingresa un exponente entero no negativo para esta implementación.")
            else:
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero para el exponente.")

    print(f"\nCalculando {base} elevado a la potencia de {exponente}...\n")

    # Llamamos a nuestra función recursiva
    resultado = potencia_recursiva(base, exponente)

    # Mostramos el resultado si se pudo calcular
    if resultado is not None:
        print(f"El resultado de {base}^{exponente} es: {resultado}")
    else:
        print("No se pudo calcular la potencia debido a un exponente no compatible.")

# Ejecutamos la función principal para probar el cálculo de potencia

probar_calculo_potencia()

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto. 

def decimal_a_binario_recursivo(decimal):
    """
    Convierte un número entero positivo en base decimal a su representación binaria
    como una cadena de texto, utilizando un enfoque recursivo.

    Args:
        decimal (int): El número entero positivo en base decimal a convertir.

    Returns:
        str: La representación binaria del número como una cadena de texto.
             Retorna una cadena vacía o un mensaje de error si la entrada no es válida.
    """
    # Manejo de casos de entrada no válidos o especiales:
    if not isinstance(decimal, int):
        print("Error: La entrada debe ser un número entero.")
        return ""
    if decimal < 0:
        print("Error: Esta función solo maneja números enteros positivos para la conversión a binario.")
        return ""
    if decimal == 0:
        # Caso base 1: Si el número es 0, su representación binaria es "0".
        return "0"
    # Este es el caso base clave para la recursión cuando el número se ha reducido completamente
    # hasta que ya no se puede dividir por 2 para obtener un cociente > 0.
    # En el momento en que el cociente de una división anterior llega a 0,
    # significa que ya hemos procesado todos los dígitos significativos.
    # Es crucial que esta condición esté después de los casos específicos 0 y negativos.
    # Técnicamente, este caso se maneja implícitamente por el retorno de la cadena vacía
    # en la primera llamada de la recursión si el número finalmente llega a 0 y no se capturó antes.
    # Para ser más explícitos y seguir la lógica de división:
    if decimal == 1:
        return "1" # El último 1 en la división sucesiva.

    # Paso recursivo:
    # 1. Calcular el residuo (será el último dígito binario para este nivel de recursión).
    residuo = decimal % 2
    # 2. Calcular el cociente (el número que se pasa a la siguiente llamada recursiva).
    cociente = decimal // 2  # Usamos división entera //

    # La recursión sucede aquí:
    # Llamamos a la función con el cociente. Cuando esa llamada recursiva retorne,
    # su resultado será la parte "izquierda" del número binario.
    # Luego, concatenamos el residuo actual (que es el dígito "derecho" para este paso).
    return decimal_a_binario_recursivo(cociente) + str(residuo)

# Parte 2: Probar la función en un algoritmo general

def probar_conversion_decimal_a_binario():
    """
    Pide al usuario un número entero positivo decimal y muestra su
    representación binaria utilizando la función recursiva.
    """
    while True:
        try:
            num_decimal = int(input("Ingresa un número entero positivo para convertir a binario: "))
            if num_decimal < 0:
                print("Por favor, ingresa un número entero positivo.")
            else:
                break # Salimos del bucle si el número es válido
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

    print(f"\nConvirtiendo el número {num_decimal} (decimal) a binario...\n")

    # Llamamos a nuestra función recursiva
    binario_resultante = decimal_a_binario_recursivo(num_decimal)

    # Mostramos el resultado
    if binario_resultante: # Si la cadena no está vacía (indicando que no hubo error)
        print(f"La representación binaria de {num_decimal} es: {binario_resultante}")
    else:
        # Esto se imprimiría si decimal_a_binario_recursivo retornó una cadena vacía por error.
        print("No se pudo realizar la conversión a binario para el número ingresado.")

# Ejecutamos la función principal para probar la conversión
probar_conversion_decimal_a_binario()

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
# lo es. 
#      Requisitos: 
# La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    """
    Verifica si una cadena de texto es un palíndromo de forma recursiva.

    Args:
        palabra (str): La cadena de texto a verificar (sin espacios ni tildes).

    Returns:
        bool: True si la cadena es un palíndromo, False en caso contrario.
    """
    # 1. CASO BASE:
    # Si la palabra tiene 0 o 1 carácter, es un palíndromo por definición.
    if len(palabra) <= 1:
        return True

    # 2. PASO RECURSIVO:
    # Verificamos si el primer carácter es igual al último carácter.
    if palabra[0] == palabra[-1]:
        # Si son iguales, entonces la palabra es un palíndromo
        # SI Y SOLO SI la subcadena sin el primer y último carácter
        # también es un palíndromo.
        # Aquí es donde ocurre la llamada recursiva.
        return es_palindromo(palabra[1:-1]) # palabra[1:-1] obtiene la subcadena
                                            # desde el segundo carácter hasta el penúltimo.
    else:
        # Si el primer y último carácter no son iguales,
        # la palabra no puede ser un palíndromo.
        return False
    
# Parte 2: Probar la función en un algoritmo general

def probar_palindromo():
    """
    Pide al usuario una palabra y verifica si es un palíndromo
    utilizando la función recursiva.
    """
    print("Vamos a verificar si una palabra es un palíndromo de forma recursiva.")
    print("Recuerda: la palabra debe ser sin espacios ni tildes.")
    print("Ejemplos de palíndromos: 'reconocer', 'anilina', 'oso'")

    palabra_usuario = input("\nIngresa una palabra: ").strip().lower()
    # .strip() elimina espacios al inicio y final
    # .lower() convierte a minúsculas para una comparación sin distinción entre mayúsculas y minúsculas

    # Aquí llamamos a nuestra función recursiva
    if es_palindromo(palabra_usuario):
        print(f"'{palabra_usuario}' ES un palíndromo.")
    else:
        print(f"'{palabra_usuario}' NO es un palíndromo.")

# Ejecutamos la función principal para probar la verificación de palíndromos

probar_palindromo()

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos. 
#      Restricciones: 
# No se puede convertir el número a string. 
# Usá operaciones matemáticas (%, //) y recursión. 
# Ejemplos: 
# suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
# suma_digitos(9)      → 9 
# suma_digitos(305)    → 8   (3 + 0 + 5) 

def suma_digitos(n):
    """
    Calcula la suma de los dígitos de un número entero positivo de forma recursiva.

    Restricciones:
    - No se puede convertir el número a string.
    - Se usan operaciones matemáticas (%, //) y recursión.

    Args:
        n (int): El número entero positivo del cual se sumarán los dígitos.

               ¡ADVERTENCIA!: Esta versión asume que 'n' ya es un entero.
                               No maneja errores de tipo de dato directamente.

    Returns:
        int: La suma de todos los dígitos del número.
             Retorna None si la entrada es negativa (ya que la consigna pide positivos).
    """
    # Manejo de entradas negativas (sigue siendo importante según la consigna de "positivo"):
    if n < 0:
        print("Error: La función suma_digitos solo acepta números enteros positivos.")
        return None

    # CASO BASE:
    # Si el número es 0, la suma de sus dígitos es 0.
    if n == 0:
        return 0

    # PASO RECURSIVO:
    # Obtenemos el último dígito del número.
    ultimo_digito = n % 10

    # Obtenemos el número sin el último dígito.
    numero_sin_ultimo_digito = n // 10

    # Suma el último dígito con la suma recursiva del resto del número.
    return ultimo_digito + suma_digitos(numero_sin_ultimo_digito)

# Parte 2: Probar la función en un algoritmo general

def probar_suma_digitos():
    """
    Pide al usuario un número entero positivo y muestra la suma de sus dígitos
    utilizando la función recursiva.
    """
    print("Vamos a calcular la suma de los dígitos de un número entero positivo.")

    while True: # Bucle para asegurar una entrada válida
        try:
            numero_ingresado = int(input("\nIngresa un número entero positivo: "))
            if numero_ingresado < 0:
                print("Por favor, ingresa un número positivo.")
            else:
                break # Salimos del bucle si el número es válido
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

    # Llamamos a nuestra función recursiva
    resultado_suma = suma_digitos(numero_ingresado)

    # Mostramos el resultado si la función no retornó None (por error de entrada)
    if resultado_suma is not None:
        print(f"La suma de los dígitos de {numero_ingresado} es: {resultado_suma}")
    else:
        print("No se pudo calcular la suma debido a una entrada no compatible.")

# Ejecutamos la función principal para probar la suma de dígitos

probar_suma_digitos()

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
# último nivel con un solo bloque. 
 
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
# pirámide. 
 
#       Ejemplos: 
# contar_bloques(1)   → 1         (1) 
# contar_bloques(2)   → 3         (2 + 1) 
# contar_bloques(4)   → 10        (4 + 3 + 2 + 1) 

def contar_bloques(n):
    """
    Calcula el total de bloques necesarios para construir una pirámide
    de forma recursiva.

    La pirámide tiene 'n' bloques en el nivel más bajo,
    (n-1) en el siguiente, y así sucesivamente hasta 1 bloque en el último nivel.

    Args:
        n (int): El número de bloques en el nivel más bajo (debe ser un entero positivo).

    Returns:
        int: El total de bloques en la pirámide.
             Retorna None si la entrada no es válida (no es un entero positivo).
    """
    # Manejo de entradas no válidas (solo números positivos):
    if n <= 0: # El nivel más bajo debe tener al menos 1 bloque
        print("Error: El número de bloques en el nivel más bajo debe ser un entero positivo.")
        return None

    # CASO BASE:
    # Si el número de bloques en el nivel actual es 1, ese es el último nivel.
    if n == 1:
        return 1

    # PASO RECURSIVO:
    # El total de bloques es el número de bloques en el nivel actual (n)
    # más el total de bloques de la pirámide que se construye a partir del nivel (n-1).
    return n + contar_bloques(n - 1)

def probar_contar_bloques():
    """
    Pide al usuario el número de bloques en el nivel más bajo de la pirámide
    y luego calcula y muestra el total de bloques utilizando la función recursiva.
    """
    print("Vamos a calcular el total de bloques necesarios para una pirámide.")
    print("En el nivel más bajo hay 'n' bloques, luego 'n-1', y así hasta 1.")

    while True: # Bucle para asegurar una entrada válida
        try:
            num_base = int(input("\nIngresa el número de bloques en el nivel más bajo (un entero positivo): "))
            if num_base <= 0:
                print("El número de bloques en la base debe ser un entero positivo (mayor que 0).")
            else:
                break # Salimos del bucle si el número es válido
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

    print(f"\nCalculando el total de bloques para una pirámide con {num_base} bloques en la base...\n")

    # Llamamos a nuestra función recursiva
    total_bloques = contar_bloques(num_base)

    # Mostramos el resultado si la función no retornó None (por error de entrada)
    if total_bloques is not None:
        print(f"El total de bloques necesarios para la pirámide es: {total_bloques}")
    else:
        print("No se pudo calcular el total de bloques debido a una entrada no compatible.")

# Ejecutamos la función principal para probar el conteo de bloques
probar_contar_bloques()

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número. 
#       Ejemplos: 
# contar_digito(12233421, 2)   → 3   
# contar_digito(5555, 5)       → 4   


def contar_digito(numero, digito):
    """
    Cuenta cuántas veces aparece un dígito específico dentro de un número entero positivo,
    utilizando un enfoque recursivo.

    Restricciones:
    - No se convierte el número a string.
    - Se usan operaciones matemáticas (%, //) y recursión.
    - No se usa isinstance.

    Args:
        numero (int): El número entero positivo donde buscar.
        digito (int): El dígito a buscar (entre 0 y 9).

    Returns:
        int: La cantidad de veces que el dígito aparece en el número.
             Retorna None si las entradas no son válidas
             (ej. numero negativo, digito fuera de rango 0-9).
    """
    # Manejo de entradas no válidas (sin isinstance):
    # Asumimos que 'numero' es un entero por el manejo en la función principal.
    if numero < 0:
        print("Error: El número debe ser un entero positivo.")
        return None
    # Asumimos que 'digito' es un entero por el manejo en la función principal.
    if not (0 <= digito <= 9):
        print("Error: El dígito a buscar debe estar entre 0 y 9.")
        return None

    # CASO BASE:
    # Si el número se ha reducido a 0, ya no hay más dígitos que contar.
    if numero == 0:
        return 0

    # PASO RECURSIVO:
    # 1. Obtener el último dígito del número actual.
    ultimo_digito = numero % 10

    # 2. Contar si el último dígito coincide con el dígito buscado.
    conteo_actual = 0
    if ultimo_digito == digito:
        conteo_actual = 1

    # 3. Preparar el número para la siguiente llamada recursiva (sin el último dígito).
    numero_restante = numero // 10

    # Sumar el conteo del dígito actual más el resultado de la llamada recursiva
    # con el resto del número.
    return conteo_actual + contar_digito(numero_restante, digito)

# Parte 2: Probar la función en un algoritmo general

def probar_contar_digito():
    """
    Pide al usuario un número y un dígito, y luego cuenta cuántas veces
    aparece ese dígito en el número utilizando la función recursiva.
    """
    print("Vamos a contar cuántas veces aparece un dígito en un número.")

    # Solicitar el número al usuario
    while True:
        try:
            num = int(input("\nIngresa un número entero positivo: "))
            if num < 0:
                print("Por favor, ingresa un número positivo.")
            else:
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

    # Solicitar el dígito a buscar al usuario
    while True:
        try:
            d = int(input("Ingresa el dígito que quieres buscar (0-9): "))
            if not (0 <= d <= 9):
                print("Por favor, ingresa un dígito entre 0 y 9.")
            else:
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un dígito entero.")

    print(f"\nBuscando el dígito '{d}' en el número '{num}'...\n")

    # Llamamos a nuestra función recursiva
    frecuencia = contar_digito(num, d)

    # Mostramos el resultado
    if frecuencia is not None: # Si la función no retornó None (por error en la función)
        print(f"El dígito '{d}' aparece {frecuencia} veces en el número {num}.")
    else:
        print("No se pudo realizar el conteo debido a una entrada no compatible en la función recursiva.")

# Ejecutamos la función principal para probar el conteo de dígitos
# Asegúrate de que esta línea NO esté comentada para ejecutar el código.
probar_contar_digito()