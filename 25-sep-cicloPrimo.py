

#Ejercicio para saber si un numero es primo 10 ciclos

'''Escribir un programa que pida al usuario un número entero
y muestre por pantalla si es un número primo o no.'''

n=int(input("Ingrese un numero por favor: "))

i = 2
while n % i != 0:
    print(f"n: {n} -> i: {i}")
    i += 1

print(f"n: {n} -> i: {i}")

if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")