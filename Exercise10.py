"""
Ejercicio 10

Un investigador de historia de la informática encontró un documento sin membrete, que data de
mitad de siglo XX, e incluye un mensaje en código morse que sospecha explicaría importantes sucesos
históricos de la posteridad. Por lo tanto, para avanzar en su investigación es necesario descifrarlo, pero
no sabe el código. Dado el siguiente diccionario que explica la codificación del código morse, ayude al
investigador en su tarea mediante un programa que le permita decodificar el mensaje.

El diccionario es útil para codificar, pero no para decodificar, intente crear un diccionario de traducción inversa.

morse = {
    'a': '.-', 'b': '-...', 'c': '-.-.',
    'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..',
    'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-',
    'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
}

code = ['.--.', '-.--', '-', '....', '---', '-.']
"""

morse = {
    'a': '.-', 'b': '-...', 'c': '-.-.',
    'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..',
    'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-',
    'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..'
},

code = ['.--.', '-.--', '-', '....', '---', '-.']


def 

traductor = {}
for element in morse.keys():
    traductor[morse[element]]=element
print(traductor)
message:str = ""
for i in code:
    message = message + traductor[i]
print(message)

