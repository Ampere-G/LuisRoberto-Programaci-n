#4 Escribe un programa en Python para ordenar un diccionario dado por clave.
#Suponiendo que pide orden de a-z en str exceptuando la ñ

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

diccionarioOrdenadoAlfabetico=dict(sorted(diccionario.items()))
diccionarioOrdenadoNumerico=dict(sorted(diccionario.items(),key=lambda x:x[1], reverse=True))

print(diccionarioOrdenadoAlfabetico)
print(diccionarioOrdenadoNumerico)
