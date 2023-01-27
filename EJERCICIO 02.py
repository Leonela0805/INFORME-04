#Escribir una función que determine la longitud de la subcadena más larga que no contiene ninguna letra repetida.
def sub_cadena(subcadena):
    for i in range(len(subcadena)):
        sc = str(subcadena[i])
        print('El número de caracteres no repetidos de la subcadena {} es: '.format(sc), longitud (sc))

def longitud(sc):
    for i in range (len(sc)):
        contador = len(sc)
        if sc[i] == sc[i-1]:
            contador -= 1
        return contador


cadena = str(input('Ingrese una cadena: '))
subcadenas = cadena.split(' ')
print(subcadenas)
sub_cadena(subcadenas)