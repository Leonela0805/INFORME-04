#Escribir una función que reemplace todas las apariciones de una subcadena en una cadena dada con otra subcadena dada.
def reemplazar(subcadena):
    print(subcadena)
    sc_remover = str(input('Ingrese la subcadena a reemplazar: '))
    for i in range(len(subcadena)):
        if subcadena[i] == sc_remover:
            nueva_subcadena = str(input('Ingrese nueva subcadena: '))
            subcadena[i] = nueva_subcadena   
    print(subcadena)

cadena = str(input('Ingrese una cadena: '))
subcadenas = cadena.split(' ')
reemplazar(subcadenas)