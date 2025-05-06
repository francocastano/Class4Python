"""
Ejercicio 6

Genere una lista con todas las tripletas pitagóricas (a, b, c) donde a, b y c son números enteros positivos
que cumplen con el teorema de Pitágoras, es decir, a^2 + b^2 = c^2. O sea que forman un triángulo rectángulo.

Para ello, genere todas las combinaciones posibles de a, b y c entre 1 y 100 con tres for anidados.
"""

tripletas: list[list[int]] = []
for a in range(1,101):
    for b in range(1,101):
        for c in range(1,101):
            if (a**2 + b**2) == c**2:
                tripletas.append([a**2,b**2,c**2])
    
print(tripletas)