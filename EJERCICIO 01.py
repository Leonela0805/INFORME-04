#Escribir una función que determine si una cadena es un palíndromo (se lee igual en ambos sentidos) o no

def palindromo(string):
    return string == string [::-1]

dato = str(input('Ingrese una cadena: '))
print(palindromo(dato))