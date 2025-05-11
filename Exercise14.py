"""
Ejercicio 14

Dada una lista de palabras que comienzan con 'a', muestre cada una en una línea.
Cuando encuentre una palabra que comienza con 'b', detenga el programa.

import random

words = ['apple', 'avocado', 'blueberry', 'apricot']

random.shuffle(words)
"""
import random

words = ['apple', 'avocado', 'blueberry', 'apricot']

random.shuffle(words)

new_words = []
"""
for i in words:
    if i[0] != "b":
        new_words.append(i)
    elif i[0] == "b":
        break

print(new_words)
"""
def until_b(list) -> list:
    for i in words:
        if i[0] != "b":
            new_words.append(i)
        elif i[0] == "b":
            break
    return new_words
print(until_b(words))