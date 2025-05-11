"""
Ejercicio 12

Dada una lista de números al azar, encuentre la primer aparición del número 0.
Asegúrese de detener el ciclo una vez que se encuentre el número,
pues no hacerlo hará que el programa tarde mucho tiempo en ejecutarse.

import random

numbers = [random.randint(0, 100) for i in range(1_000_000)]
"""

import random
numbers = [random.randint(0, 100) for i in range(1_000_000)]

def found_0(number):
    random_numbers = []
    for i in numbers:
        random_numbers.append(i)
        if i == 0:
            break
    return random_numbers
print(found_0(numbers))
