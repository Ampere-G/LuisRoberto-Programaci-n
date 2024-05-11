#Histograma numeros aleatorios
import random


def HistogramaNumAleatorios(min,max,numElementos,numClasificaciones):
    rangoValor=max/numClasificaciones
    histograma={}
    elementos=[random.uniform(min,max) for x in range(numElementos)]
    elementos.sort
    
    for i in range(numClasificaciones):
        minimo=i*rangoValor
        maximo=minimo+rangoValor
        
        clave=f'[{round(minimo,2)},{round(maximo,2)}]'
        l=[]
        for j in elementos:
            if j>=minimo and j<=maximo:
                l.append(j)
        
        histograma[clave]=len(l)
        
        minimo=maximo
                
        
    return histograma

def imprimirDiccionarios(diccionario,titulo=''):
    print(f'''
          
{titulo}''')
    for key,value in diccionario.items():
        print(f'{key}={value}')

imprimirDiccionarios(HistogramaNumAleatorios(0,1,50,10),'50 elementos')

imprimirDiccionarios(HistogramaNumAleatorios(0,1,1000,10), '100 elementos')


            
        
        
    
