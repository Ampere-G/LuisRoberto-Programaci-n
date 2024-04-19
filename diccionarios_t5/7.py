#7 Escribe un programa en Python para eliminar duplicados del diccionario.

#Un diccionario no puede tener keys repetidas, así que supondré que se refiere a los values

diccionario=dict(a=1,b=10,c=100,d=200,g=0,e=5,f=60,t=100,z=10)

def eliminarduplicados(diccionario):
    diccionarioNoDup={}
    for key,value in diccionario.items():
        if value not in diccionarioNoDup.values():
            diccionarioNoDup[key]=value
    
    return diccionarioNoDup

diccionarioNoDup=eliminarduplicados(diccionario)

print(diccionarioNoDup)