import libreriaMatrices as ls
import math


def half_value(vector,vector1):
    tmp=ls.multiplicacion_complejas(vector,vector1)
    matrix=ls.matriz_conjugada(tmp)
    complejo=(0,0)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            a,b=matrix[i][j],vector1[i][j]
            real=(a[0]*b[0])-(a[1]*b[1])
            ima=(a[0]*b[1])+(a[1]*b[0])
            c1=complejo;c2=(real,ima)
            complejo=((c1[0]+c2[0]),(c1[1]+c2[1]))
    return complejo

def variance(vector,vector1):
    matrixtmp=ls.matriz_adjunt(vector)
    half_val=half_value(matrixtmp,vector1)
    b=[[(0,0) for i in range(len(matrixtmp))]for j in range(len(matrixtmp[0]))]
    for i in range(len(matrixtmp)):
        for j in range(len(matrixtmp[0])):
            if i !=j: b[i][j]=half_val
    a=[[(0,0) for i in range(len(matrixtmp))]for j in range(len(matrixtmp[0]))]
    for i in range(len(matrixtmp)):
        for j in range(len(matrixtmp[0])):
            a[i][j]=(matrixtmp[i][j][0]-b[i][j][0],matrixtmp[i][j][1]-b[i][j][1])
   
    tmp1=ls.multiplicacion_complejas(a,a)

    kkk = [[(0,0) for j in range(len(vector1))] for i in range(len(vector1[0]))]

    for i in range(0,len(vector1[0])):
        for j in range(0,len(vector1)):
            kkk[i][j]=vector1[j][i]
    print(len(kkk))
    matriz=[]
    for i in range(0,len(kkk)):
        vector=[]
        for j in range(0,len(kkk[0])):
            vector.append((kkk[i][j][0],kkk[i][j][1]*-1))        
        matriz.append(vector)
     
    tmp=ls.multiplicacion_complejas(matriz,tmp1)
    complejo=(0,0)
    print(matriz)
    print(matriz)

    for i in range(len(tmp[0])):
        for j in range(len(tmp)):
     
            a,b=tmp[i][j],vector1[i][j]
            real=(a[0]*b[0])-(a[1]*b[1])
            ima=(a[0]*b[1])+(a[1]*b[0])
            c1=complejo;c2=(real,ima)
            complejo=((c1[0]+c2[0]),(c1[1]+c2[1]))
    return complejo

        
