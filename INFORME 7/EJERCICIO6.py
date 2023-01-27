#EJERCICIO 6:Escribir una función que reemplace todas las apariciones
#de una subcadena en una cadena dada con otra subcadena
#dada .
import re
print("Ejercicio 6")


def reemplazo_palabra(cadena, subcadena, subcadena_cambio):
    return re.sub(subcadena, subcadena_cambio, cadena)


pala = "El amor es una locura que ni el cura lo cura y si el cura lo cura es una locura del cura."
subcadena = "cura"
subcadena_cambio = " dx (xddddd...)"
print(reemplazo_palabra(pala, subcadena, subcadena_cambio))