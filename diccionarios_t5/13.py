#13 Escribe un programa en Python para obtener la profundidad de un diccionario.

def valorProfundidadDiccionario(diccionarioAnidado):
    if type(diccionarioAnidado)!=dict:
        return 0
    if not diccionarioAnidado:
        return 1
    
    return 1+ max(valorProfundidadDiccionario(diccionarios) for diccionarios in diccionarioAnidado.values())

DiccionarioAnidado={
    'Dict1': {'names': {'Moises','Pedro'}, 
              'ages': {'19','20','17'}}, 
    
    'Dict2': {'name': 'Bob', 
              'age': '25'}
                    }

print(valorProfundidadDiccionario(DiccionarioAnidado))
