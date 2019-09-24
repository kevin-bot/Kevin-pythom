
#practica para asentuar los conocimientos de dias dom,22 de sep,21:54


'''1.DEFINIR  una funcion max() que tome como argumento dos números y
devuelva el mayor de ellos'''
def funcion(numerouno,numerodos):
    if numerouno < numerodos:
        print(f" {numerodos} es  mayor que {numerouno}")
    elif numerouno>numerodos:
        print(f"{numerouno}  es mayor que {numerodos}")
    else :
        print(f"Son el mismo numero ")
if __name__ == '__main__':
    num1 = float(input("ingresa un nemero: "))
    num2 = float(input("ingresa otro nemero: "))
    funcion(num1,num2)
