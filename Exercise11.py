"""
Ejercicio 11

Dada una lista de números y un número, determine en qué posición se encuentra el número en la lista.
Si no se encuentra, que el programa muestre -1. Utilice break al encontrar el número.

numbers = [11, 25, 3, -4, 95]
n = 3
"""

numbers = [11, 25, 1, -4, 95]
n = 3

def is_there(numbers,number) -> str | int:
    found = False
    for i in numbers:
        if i == number:
            found = True
            return f"el numero {number} esta en la posicion {numbers.index(i)}"
    if found == False:
        return -1

print(is_there(numbers,n))
