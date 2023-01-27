# EJERCICIO 1:Escribir una función que determine si una cadena es un
#palíndromo (se lee igual en ambos sentidos) o no :
def Reversa(palabra):
    reversa = palabra[::-1]
    if palabra == reversa:
        print("La palabra ingresada si es palindromo!...")
    else:
        print("La palabra ingresada no es palindromo!...")
palabra = input("Ingrese una palabra: ").lower()
x = Reversa(palabra)
print(x)