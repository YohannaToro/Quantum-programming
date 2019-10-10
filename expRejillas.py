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
    tmp=[[(0,0) for i in range(len(prob[0]))] for j in range(len(prob))]
    for i in range(slits):
        tmp[i][0]=(math.sqrt(1/slits),0)
    for i in range(slits+1,len(prob)):
        tmp[i][i]=(1,0)
    vector=[(0,0) for i in range(n)]
    for i in range(n):
        if i ==0: vector[i]=(1,0)
    respuesa=libreriaMatrices.multiplicacionDeMatricesComplejas(tmp,tmp)
    
    return respuesa
def prepare_states(slits,target, prob):
    n = slits + 1
    n1 = 2 * slits + n * target + 1
    probabilityTargets = len(prob)
    ExperimentalMatrix= [[(0, 0) for j in range(n1)]for i in range(n1)]
    return (ExperimentalMatrix,probabilityTargets)

def multipleRendijaCuantico(slits,target, prob):
    pos=0
    res=prepare_states(slits,target, prob)
    ExperimentalMatrix,probabilityTargets=res[0],res[1]
    for i in range(1, slits + 1):
        ExperimentalMatrix[i][0]= (1/(slits**(1/2)),0)
        pos = i
    for i in range(1, slits + 1):
        for j in range(pos, pos + probabilityTargets  + 1):
            ExperimentalMatrix[j][i] =prob[i-1]
    return ExperimentalMatrix
