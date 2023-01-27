#EJERCICIO 4:Escribir una función que determine la frecuencia de cada
#carácter en una cadena dada y devuelva un diccionario .
def Diccionario_texto(texto):
    retiro = ".;:.\n\"'"
    for i in retiro:
        texto = texto.replace(i,"")
    texto.lower()
    list_palabras = texto.split(" ")
    diccionario = {}
    for i in list_palabras:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    for j in diccionario:
        cantidad = diccionario[j]
        print(f"Palabra {j} se repite {cantidad}")
Diccionario_texto("Yo no compro coco porque como poco coco, como poco coco como, poco coco compro.")
