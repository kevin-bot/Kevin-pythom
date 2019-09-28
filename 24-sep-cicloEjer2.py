

#Ejercicio con ciclos

'''Escribir un programa que almacene la cadena de caracteres
 contraseña en una variable, pregunte al usuario
 por la contraseña hasta que introduzca la contraseña correcta.'''

key="kevin"

contraseña=str(input("Ingrese su password: "))
numero=int(input("Ingrese un numero por favor: "))

while contraseña != key:
    contraseña = str(input("Ingrese su password: "))

