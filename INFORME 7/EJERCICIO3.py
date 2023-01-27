#EJERCICIO 3:Escribir una función que divida una cadena dada en una
#lista de subcadenas cada vez que aparezca un carácter
#específico  .
def SEPARACION_C(cadena, caracter):
    cadena_separada = cadena.split(caracter)
    return cadena_separada

print(SEPARACION_C("ESPACIO TXT", " "))
