"""
Ejercicio 3

Imprima una cuenta regresiva, comenzando en 10 y terminando en 0, pero que en vez de imprimir el 0, imprima "¡Feliz Año Nuevo!".
"""
# message = "Feliz año nuevo"
# for i in range(10,-1,-1):
#     if i > 0:
#         print(i)
#     if i == 0:
#         print(message)

def happy_new_year() -> str:
    message = list[str]()
    for i in range(10,0,-1):
        message.append(str(i))
    message.append("Happy new year")
    return "\n".join(message)
print(happy_new_year())