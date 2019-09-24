
#practica 3
'''Definir una funcion inversa() que calcule
la inversion de una cadena. Por ejemplo la cadena
"estoy porbando deberia devolver “odnaborp yotse”'''


def reverse(texto):
    texto2 =texto[::-1]
    print(f"{texto} al reves es : {texto2}")
if __name__=="__main__":
    palabra = str(input("Escribe algo: "))
    reverse(palabra)