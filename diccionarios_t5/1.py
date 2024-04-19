#Escribe un programa en Python para multiplicar todos los elementos de un diccionario.

numeros=dict(a=2,b=5,c=7,d=8)
resultado=1
for numero in numeros.values():
    resultado*=numero

print('resultado:',resultado)