#Tarea 4

#Hacer un diccionario con el nombre de 10 alumnos de preparatoria con las calificaciones

Calificaciones={
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

def busqueda(diccionario,calificacion=False,nombre=False):
    resultado=[]
    for nombres,calificaciones in diccionario.items():
        if calificacion and calificaciones==calificacion:
                resultado.append((nombres,calificaciones))
            
        if nombre and nombre==nombres:
                resultado.append((nombres,calificaciones))
        else: return
        imprimir(resultado)

def imprimir(iterable):
    print(f'Nombre:Calificación')
    if type(iterable)==list:
        for i in iterable:
            nombre=i[0]
            calificacion=i[1]
            print(f'{nombre}:{calificacion}')
            
    if type(iterable)==dict:
        for nombre,calificacion in iterable.items():
            print(f'{nombre}:{calificacion}')
            
        
  
print(f'''Acciones:
    (1) Buscar nombres por calificación.
    (2) Buscar calificaciones por nombre.
    (3) Ordenar alfabéticamente.
    (4) Ordenar de mayor a menor calificación.
       
      ''')

accion=int(input('INGRESE LA ACCIÓN DESEADA Y PULSE ENTER:'))

match accion:
    case 1:
        calificacionDeseada=int(input("Ingrese la calificación deseada a buscar:"))
        nombreDeseado=False
        busqueda(Calificaciones,calificacionDeseada,nombreDeseado)
    case 2:
        nombreDeseado=(input("Ingrese el nombre deseado a buscar:"))
        calificacionDeseada=False
        busqueda(Calificaciones,calificacionDeseada,nombreDeseado)
    case 3:
        sortedNombres = dict(sorted(Calificaciones.items()))
        imprimir(sortedNombres)
    
    case 4:
        sortedCalificaciones= dict(sorted(Calificaciones.items(),key=lambda x:x[1],reverse=True))
        imprimir(sortedCalificaciones)

        


