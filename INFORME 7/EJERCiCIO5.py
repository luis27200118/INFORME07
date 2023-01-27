#EJERICICIO 5: Escribir una función que determine la longitud de la
#subcadena más larga que contiene solo dígitos .
def SUBCADENA_L(palabra):
    subcadenas = palabra.split()
    lista_cadenas = []
    for i in subcadenas:
        lista_cadenas.append(len(i))
    for j in subcadenas:
        if len(j) == max(lista_cadenas):
            return str(i) + " de valor : " + str(len(j))


print("Valor de la cadena mas larga : "+SUBCADENA_L(
    "a la vivora la víbora, víbora, de la mar, de la mar, Los de adelante corren mucho y los de atrás se quedarán, tras, tras, tras, traaas. Una mexicana que frutos vendía, ciruela, chabacano, melón o sandígaaaaaaaaaaaa "))
