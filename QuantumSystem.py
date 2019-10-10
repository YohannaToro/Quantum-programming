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
