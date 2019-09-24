
#Ejercicio numero 2

'''Escribir una funcion que tome un caracter y debulva
True si es una vocal, de lo contrario devulve False'''


def funcionbocal (vocal):
    if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
        return  True
    else:
        return False
if __name__=="__main__":
    letra = str(input("Ingrese una letra : "))

    verdaderoofalso=funcionbocal(letra)
    if verdaderoofalso:
        print("es vocal")
    else:
        print(f"No es vocal")