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
    print(min)
get_min_number(numbers)

def get_max_number(numbers:list) -> int:
    max:int = numbers[0]
    for i in numbers:
        if i >= max:
            max = i
    print(max)
get_max_number(numbers)

def get_min_and_max(numbers:list) -> list:
    min:int = get_min_number(numbers)
    max:int = get_max_number(numbers)
    min_and_max = (min,max)
    return min_and_max
print(get_min_and_max(numbers))
