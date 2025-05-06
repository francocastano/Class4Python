"""
Ejercicio 5

Determine si un número ingresado es primo o no. Un número es primo si es divisible únicamente por 1 y por sí mismo.

Opcional: determine todos los números primos entre el 1 y el 100 inclusive. Se puede lograr con un for dentro de otro.
"""

def is_prime(number:int) -> bool:
    for i in range(2,number,1):
        if  not(number % i):
            return False
    return True
print(is_prime(9))

# def get_prime_until_onehundred() -> list[int]:
#     primes: list[int] = []
#     for i in range(2,101,1):
#         if is_prime(i):
#             primes.append(i)
#     return primes



def get_prime_until_onehundred() -> list[int]:
    primes: list[int] = []
    for i in range(2,101,1):
        for j in range(2,i,1):
            if not(i % j):
                break
        else:
            primes.append(i)
    return primes

print(get_prime_until_onehundred())