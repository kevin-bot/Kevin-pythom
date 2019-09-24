

#Ejercicio de condicional

'''Los alumnos de un curso se han dividido en
dos grupos A y B de acuerdo al sexo y el nombre.
 El grupo A esta formado por las mujeres con un
  nombre anterior a la M y los hombres con un
   nombre posterior a la N y el grupo B por el
   resto. Escribir un programa que pregunte al
    usuario su nombre y sexo, y
 muestre por pantalla el grupo que le corresponde.'''

nombre=str(input("Ingrese su nombre : ")).lower()
sexo=str(input("Ingrese su sexo M o F : "))

primerLetraNombre=nombre[0:1]
grupo=""
if sexo=="m":
    if primerLetraNombre<"m":
       grupo="A"
    else:
        grupo="B"
else:
    if primerLetraNombre>"n":
        grupo="A"
    else:
        grupo="B"

print(f"Usted pertenece al grupo {grupo}")