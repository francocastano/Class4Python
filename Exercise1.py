"""
Ejercicio 1

De todos los números entre el 1 y el 100 inclusive, imprima los números que son múltiplos de 3 y de 5.
Recuerde que para verificar divisibilidad puede utilizar el operador % (módulo) que devuelve el resto de la división entre dos números.

Opcional: resuelva el problema Fizz Buzz tradicional de las entrevistas de programación:
https://en.wikipedia.org/wiki/Fizz_buzz
"""

# for i in range(1,101):
#     if not(i % 3) and not(i % 5):
#         print(i)

def multiplies3and5of100() -> list[int]:
    numbers=[]
    for multiplies in range(1,100):
        if not(multiplies % 3) and not(multiplies % 5):
            numbers.append(multiplies)
    return numbers
print(multiplies3and5of100())