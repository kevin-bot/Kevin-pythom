

#Ejercicios condicionales 23-sep

'''Escribir un programa que pida al usuario
dos números y muestre por pantalla su
 división. Si el divisor es cero el
 programa debe mostrar un error.'''

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
if num2 == 0:
    print("Error")
else:
    print(f"La division es : {num1/num2}")

