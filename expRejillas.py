import libreriaMatrices
import math
"""Los experimentos de la canicas con coeficiente booleanos"""
def experimentoCanicas(matriz,estadoIni,numCambios):
    estadoIni=libreriaMatrices.transpuesta_vector(estadoIni)
    for i in range(numCambios):
        estadoIni=libreriaMatrices.multiplicacionDeMatricesComplejas(matriz,estadoIni)
    return estadoIni
def multipleRendijasClasico(slits,targets,prob):
    n=slits+targets+1
    tmp=[[(0,0) for i in range(len(prob[0]))] for j in range(prob)]
    for i in range(slits):
        tmp[i][0]=(math.sqrt(1/slits),0)
    for i in range(slits+1,len(prob)):
        tmp[i][i]=(1,0)
    vector=[(0,0) for i in range(n)]
    for i in range(n):
        if i ==0: x[i]=(1,0)
    respuesa=libreriaMatrices.multiplicacionDeMatricesComplejas(tmp,tmp)
    
    return respuesta

def multipleRendijaCuantico(slits,targets,prob):
    n=slits+targets+1
    tmp=[[(0,0) for i in range(len(prob[0]))] for j in range(prob)]
    for i in range(slits):
        tmp[i][0]=(1/slits)
    for i in range(slits+1,len(prob)):
        tmp[i][i]=1
    vector=[0 for i in range(n)]
    for i in range(n):
        if i ==0: x[i]=1
    respuesa=libreriaMatrices.multiplicacionDeMatricesComplejas(tmp,tmp)
    
    return respuesta
