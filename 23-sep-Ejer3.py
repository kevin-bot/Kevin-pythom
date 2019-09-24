

#Ejercicio

'''Escribir esta operacion y muestre el resultado'''

#print(((3+2)/(2*5))**2)

'''Escribir un programa que pida al usuario dos
 números enteros y muestre por pantalla la <n> entre
  <m> da un cociente <c> y un resto <r> donde <n> y <m> 
  son los números introducidos por el usuario, y <c> y <r> son el cociente
 y el resto de la división entera respectivamente.'''


peso=float(input("Ingrese su péso: "))
estatura=float(input("Ingrese su Estatura: "))

#imc=round((peso)/(estatura)**2,2)
imc=(peso)/(estatura)**2

print(f"Tú indice de masa corporal es {imc:.2f}")

