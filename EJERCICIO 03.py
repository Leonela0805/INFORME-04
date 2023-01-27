#Escribir una función que divida una cadena dada en una lista de subcadenas cada vez que aparezca un carácter específico.
cadena = str(input('Ingrese una cadena: '))
caracter = str(input('Ingrese el caracter que dividira la cadena: '))
print(cadena.split(caracter))