import libreriaMatrices as ls
import math

def probability_specific_position(vector,pos):
    return float("%.6f" % (ls.norma_matrices([[vector[pos]]])**2/ls.norma_matrices([vector])**2))
    
def Transitional_amplitude(m1,m2):    
    tmp=ls.multiplicacion_complejas(m1,ls.transpuesta_vector(ls.matriz_conjugada(m2)[0]))
    a=0;b=0
    for i in range(len(tmp)):
        a+=float("%.4f" % (tmp[0][0][0]));b+=float("%.4f" % (tmp[0][0][1]))

    return (a,b)

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

def system_value(time,vertex,array):
   
    for i in range(time):
        vertex=ls.multiplicacion_complejas(array[i],vertex)
    return vertex

def variance(vector,vector1):
    matrixtmp=ls.matriz_adjunt(vector)
    half_val=half_value(matrixtmp,vector1)
    b=[[(0,0) for i in range(len(matrixtmp))]for j in range(len(matrixtmp[0]))]
    for i in range(len(matrixtmp)):
        for j in range(len(matrixtmp[0])):
            if i !=j: b[i][j]=half_value
    a=[]
    for i in range(0,len(m1)):
        vec=[]
        for j in range(0,len(m1[0])):
            vec.append((matrixtmp[i][j][0]-b[i][j][0],matrixtmp[i][j][1]-b[i][j][1]))
        a.append(vector)
    tmp1=ls.multiplicacion_complejas(a,a)
    vector1=ls.matriz_adjunt(vector1)
    tmp=ls.multiplicacion_complejas(vector1,tmp1)
    complejo=(0,0)
    for i in range(len(tmp)):
        for j in range(len(tmp[0])):
            a,b=matrix[i][j],vector1[i][j]
            real=(a[0]*b[0])-(a[1]*b[1])
            ima=(a[0]*b[1])+(a[1]*b[0])
            c1=complejo;c2=(real,ima)
            complejo=((c1[0]+c2[0]),(c1[1]+c2[1]))
    return complejo

        
