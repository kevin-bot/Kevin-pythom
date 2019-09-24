

#Ejercicio 5

'''Escribir un programa
 que almacene la cadena de caracteres contraseña en una
 variable, pregunte al usuario por la contraseña e
  imprima por pantalla si la contraseña introducida
   por el usuario coincide con la guardada en la variable
    sin tener en cuenta mayúsculas y minúsculas'''

password="kevin"

passwordIngresado=str(input("Escriba la contraseña: ")).lower()

if password == passwordIngresado:
    input(f"Las contaseña es corracta¡¡")
else:
    input(f"Las contaseña es incorracta¡¡")