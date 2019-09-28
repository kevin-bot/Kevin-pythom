

#Ejercico de condicional anidado

'''Los tramos impositivos para la declaración de la renta en un
determinado país son los siguientes:
Renta 	Tipo impositivo
Menos de 10000€ 	5%
Entre 10000€ y 20000€ 	15%
Entre 200000€ y 35000€ 	20%
Entre 350000€ y 60000€ 	30%
Más de 60000€ 	45%

Escribir un programa que pregunte al usuario su renta anual y
 muestre por pantalla el tipo impositivo que le corresponde.'''

rentaDeUsuario=float(input("Ingrese su renta: "))

if rentaDeUsuario<=10000:
    print(f"Tipo de impositivo es : 5% ")
elif rentaDeUsuario<=20000:
    print(f"Tipo de impositivo es : 15% ")
elif rentaDeUsuario<=35000:
    print(f"Tipo de impositivo es : 20% ")
elif rentaDeUsuario<=60000:
    print(f"Tipo de impositivo es : 30% ")
else:
    print(f"Tipo de impositivo es : 45% ")