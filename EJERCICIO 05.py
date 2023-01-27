#Escribir una función que determine la longitud de la subcadena más larga que contiene solo dígitos.
def longitud(subcadena):
    for i in range(len(subcadena)):
        sc = str(subcadena[i])
        if sc.isdecimal() is True:
            print('La longitud de la subcadena {} es: '.format(sc), len(sc))


cadena = str(input('Ingrese una cadena: '))
subcadenas = cadena.split(' ')
print(subcadenas)
longitud(subcadenas)