"""
Ejercicio 2

Sume todos los números pares entre el 1 y el 100 inclusive. El resultado esperado es 2550.
"""
# acc = 0  
# for i in range(1,101):
#     if not(i % 2):
#         acc = acc + i
# print(acc)

def getTheSumOfcoupleNumbersOf100() -> int:
    acc= 0
    for i in range(1,101):
        if not(i % 2):
            acc = acc + i
    return acc
print(getTheSumOfcoupleNumbersOf100())