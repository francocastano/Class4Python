"""
Ejercicio 7

Dado un texto cualquiera, determine cuántas veces aparece cada vocal en el texto. No distinga entre mayúsculas y minúsculas.
Recuerde que puede iterar por sobre las letras de un texto utilizando el for solamente. Recuerde el método lower.

Comience con el siguiente diccionario:

vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

Opcional: comience con un diccionario vacío y cuente cualquier letra. A medida que aparezcan nuevas, agréguelas.
"""
vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

text = "hola"
# count:int = 0 
# for i in text:
#     for j in list(vowels):
#         if j == i:
#             count = count + 1
    

def get_amout_of_vowels(word:str) -> int:
    count:int = 0
    for i in word:
        for j in list(vowels):
            if j == i:
                count = count + 1
    return count

print(get_amout_of_vowels("paso la noche"))