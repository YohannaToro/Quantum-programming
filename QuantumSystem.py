import libreriaMatrices as ls
import math

def probability_specific_position(vector,pos):
    return float("%.6f" % (ls.norma_matrices([[vector[pos]]])**2/ls.norma_matrices([vector])**2))
def norme_ket(ket):
    return ls.multiplicacion_escalar_matrices((1/ls.norma_matrices(ket),0),ket)
def Bra(m):
    return ls.transpuesta_vector(ls.matriz_conjugada(m)[0]);
    
def Transitional_amplitude(m1,m22):    
    tmp=ls.multiplicacionDeMatricesComplejas(m1,Bra(m2))
    a=0;b=0
    for i in range(len(tmp)):
        a+=float("%.4f" % (tmp[0][0][0]));b+=float("%.4f" % (tmp[0][0][1])) 
    return (a,b)
