

#Ejercicio 4

'''Escribir un programa que pregunte el nombre del
usuario en la consola y un número entero e imprima
por pantalla en líneas distintas el nombre del usuario
tantas veces como el número introducido.'''

nombre_usuario=str(input("Ingrese su nombre de usuario: "))
numero_randon=int(input("Ingrese un numero: "))


print((nombre_usuario+"\n")*numero_randon)