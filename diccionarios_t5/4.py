#4 Escribe un programa en Python para ordenar un diccionario dado por clave.
#Suponiendo que pide orden de menor a mayor en numeros y de a-z en str exceptuando la ñ claro

diccionario={
    'Diana':10,
    'Roberto':10,
    'Emily':7,
    'Christian':6,
    'Luis':9,
    'Alberto':5,
    'Ulises':8,
    'Cristian':5,
    'Cesar':9,
    'Libier':7
    
            }

diccionarioOrdenado=dict(sorted(diccionario.items()))

print(diccionarioOrdenado)
