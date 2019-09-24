
# practicando for

'''mostrar los caracteres de un acadena'''

cadena=str(input("Ingrese la cadena que quiera: ").lower())

for i in cadena:
    vocal= i
    if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
        print(f" Vocal : {i}")
    else :
        print(f"consonante :{i}")


