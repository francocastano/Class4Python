"""
Ejercicio 9

Escriba los siguientes programas sin utilizar métodos de lista.

a. Dada una lista de números, calcule el mínimo y el máximo de la lista. Nota: es posible hacerlo
recorriendo una única vez la lista o recorriéndola dos veces. Piense las ventajas y desventajas de
ambos métodos.

numbers = [11, 25, 3, -4, 95]

# El programa debería mostrar -4 y 95

b. Dada una lista palabras, cree una nueva lista formada sólo por aquellas que comienzan con "a".

words = ["arbol", "barco", "artificial", "casa", "dado", "a"]

# El programa debería mostrar
["arbol" , "artificial" , "a"]
"""

numbers = [11, 25, 3, -4, 95]
words = ["arbol", "barco", "artificial", "casa", "dado", "a"]

def get_min_number(numbers:list) -> int:
    min:int = numbers[0]
    for i in numbers:
        if i <= min:
            min = i
get_min_number(numbers)

def get_max_number(numbers:list) -> int:
    max:int = numbers[0]
    for i in numbers:
        if i >= max:
            max = i
get_max_number(numbers)

def get_min_and_max(numbers:list) -> list:
    min_and_max = []
    min:int = get_min_number(numbers)
    max:int = get_max_number(numbers)
    min_and_max.append(min)
    min_and_max.append(max)
    return min_and_max

    

print(get_min_and_max(numbers))

def words_stats_a(words:list) -> list:
    a_words = []
    for caracter in words:
        if caracter[0] == "a":
            a_words.append(caracter)
    return a_words
print(words_stats_a(words))