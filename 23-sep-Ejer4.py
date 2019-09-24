


# Ejercicio 4

'''Escribir un programa que pregunte al usuario una cantidad a
    invertir, el interés anual y el número de años,
 y muestre por pantalla el capital obtenido en la inversión'''

cantidadInvertir=float(input("Ingrese la cantidad a invertir: "))
interesAnual=float(input("Ingrese el interes anual: "))
numeroDeAños=int(input("Ingrese el numero de años : "))

capital=cantidadInvertir*(interesAnual/100+1)**numeroDeAños
print(f"{capital:.2f}")