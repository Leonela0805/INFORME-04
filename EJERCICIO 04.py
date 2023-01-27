#Escribir una función que determine la frecuencia de cada carácter en una cadena dada y devuelva un diccionario.
def frecuencia(c):
    diccionario = {}
    for i in range (len(c)):
        caracter = c[i]
        f = c.count(caracter)
        diccionario.setdefault(caracter,f)
    print(diccionario)

cadena = str(input('Ingrese una cadena: '))
frecuencia(cadena)