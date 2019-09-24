
#Ejercicio 2

'''Escribir un programa que pregunte el nombre del
usuario en la consola y después de que el usuario
lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y
 <n> es el número de letras que tienen el nombre.'''


nombreUsuario=str(input("Ingrese su nombre de usuario"))
print(f"{nombreUsuario} tiene {len(nombreUsuario)} letras ")
