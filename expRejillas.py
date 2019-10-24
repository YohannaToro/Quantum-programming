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
    n = slits + 1
    n1 = 2 * slits + n * target + 1;n2=1/3
    probabilityTargets = len(prob)
    ExperimentalMatrix=prob
    pos=0
    res=prepare_states(slits,target, prob)
    ExperimentalMatrix,probabilityTargets=res[0],res[1]
    for i in range(1, slits + 1):
        ExperimentalMatrix[i][0]= (1/(slits**(1/2)),0)
        pos = i
    for i in range(1, slits + 1):
        for j in range(pos, pos + probabilityTargets  + 1):
            ExperimentalMatrix[j][i] =(n2,0)
    vector=[]
    for i in range(n1):
        if i==0: vector.append((1.0,0))
        else: vector.append((0,0))
    resMatrix=libreriaMatrices.multiplicacion_complejas(ExperimentalMatrix,ExperimentalMatrix)
    res=0
    rs=[];real=0;ima=0
    for i in range(len(vector)):
        x1=0;x2=0
        for j in range(len(resMatrix[0])):
            c1=resMatrix[i][j];c2=vector[j]
            x1=c1[0]*c2[0];x2=c1[1]*c2[1]
            rs.append((x1,x2))
    return rs
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
