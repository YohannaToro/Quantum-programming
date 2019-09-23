import libreriaMatrices
"""Los experimentos de la canicas con coeficiente booleanos"""
def experimentoCanicas(matriz,estadoIni,numCambios):
    for i in range(numCambios):
        estadoini=cambios(matriz,estadoini)
    return estadoini
def multipleRendijasClasico(s,t,prob):
    n=s+t+1
    for i in range(s):
        prob[i][0]:prob=1.0/s
    
    for i in range(s+1,len(prob)):
        prob[i][i]:prob=1.0
    return multpilicar(prob,prob)
def multipleRendijaCuantico(s,t,prob):
    n=s+t+1
    for i in range(s):
        prob[i][0]:prob=complex(1.0/s)
    
    for i in range(s+1,len(prob)):
        prob[i][i]:prob=complex(1,0)
    return libreriaMatrices.multiplicacion_matrices(prob,prob)

def cambios(matriz,estadoini):
    res=0
    vector=[]
    for i in range(len(estdoini)):
        for j in range(len(estadoini[0])):
            res+=(matriz[i]*matrz[j])
            
        vector.append(res);res=0
    return vector
def prueba(m):
    return libreriaMatrices.transpuesta(m)
    
