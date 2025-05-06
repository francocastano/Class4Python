"""
Ejercicio 4

Dado un string cualquiera, cree otro string nuevo dado vuelta, sin utilizar el método reverse.

word = "Python"

# El resultado esperado es "nohtyP"
"""

word = "Python"
# reverse_word :list[str] = []
# for i in range(len(word)-1,-1,-1):
#     reverse_word.append(word[i])
# print("".join(reverse_word))


# def reverse_word(word:str):
#     phase = list[str]()
#     for i in range(len(word)-1,-1,-1):
#         phase.append(word[i])
#     return "".join(phase)

def reverse_word(word:str):
    return word[::-1]


print(reverse_word(word))