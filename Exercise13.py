"""
Ejercicio 13

Dada la lista inicial [0, 1], agregue 100 veces la suma de los dos últimos números de la lista.
Detenga el programa si la suma de los dos últimos números es mayor a 1000.
Esta es una forma de generar la secuencia de Fibonacci.

numbers = [0, 1]
"""

numbers = [0, 1]

for i in range(1,101):
    if numbers[len(numbers)-1] < 1000:
        numbers.append(numbers[len(numbers)-2] + numbers[len(numbers)-1])
    
print(numbers)

def fibonacci_until_thousand():
    for i in range(1,101):
        if numbers[len(numbers)-1] < 1000:
            numbers.append(numbers[len(numbers)-2] + numbers[len(numbers)-1])
    return numbers
print(fibonacci_until_thousand())