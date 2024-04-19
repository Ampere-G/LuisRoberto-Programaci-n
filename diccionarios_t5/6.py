#6 Escribe un programa en Python para obtener un diccionario a partir de los campos de un objeto.

class Computadora:
    def __init__(self):
        self.marca='msi'
        self.ram='8gb'
        self.procesador='intel i7 9na generación'
        self.grafica='RTX 3090'
        
computadora=Computadora()

#Usando vars
diccionarioCampos=vars(computadora)
print(diccionarioCampos)

#sin usar vars

def diccionarioOfCampos(objeto):
    return {
        'marca':objeto.marca,
        'ram':objeto.ram,
        'procesador':objeto.procesador,
        'gráfica':objeto.grafica
        
    }

print(diccionarioOfCampos(computadora))
        