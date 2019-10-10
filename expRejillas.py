import libreriaMatrices
import math
"""Los experimentos de la canicas con coeficiente booleanos"""
def multipleRendijasClasico(slits,target, prob):
    pos=0
    res=prepare_statesClasico(slits,target, prob)
    ExperimentalMatrix,probabilityTargets=res[0],res[1]
    for i in range(1, slits + 1):
        ExperimentalMatrix[i][0]= 1/(slits**(1/2))
        pos = i
    for i in range(1, slits + 1):
        for j in range(pos, pos + probabilityTargets  + 1):
            ExperimentalMatrix[j][i] =prob[i-1]
    return ExperimentalMatrix
def prepare_states(slits,target, prob):
    n = slits + 1
    n1 = 2 * slits + n * target + 1
    probabilityTargets = len(prob)
    ExperimentalMatrix= [[(0, 0) for j in range(n1)]for i in range(n1)]
    return (ExperimentalMatrix,probabilityTargets)
def prepare_statesClasico(slits,target, prob):
    n = slits + 1
    n1 = 2 * slits + n * target + 1
    probabilityTargets = len(prob)
    ExperimentalMatrix= [[0 for j in range(n1)]for i in range(n1)]
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
def experimento_Canicas(matriz,estadoIni,numCambios):
    for i in range(numCambios):
        estadoIni=cambios(matriz,estadoIni)
    return estadoIni
def cambios(matriz,estadoini):
    res=0
    vector=[]
    for i in range(len(estadoini)):
        for j in range(len(estadoini)):
            res+=matriz[i][j]*estadoini[j]

        vector.append(res);res=0
    return vector
