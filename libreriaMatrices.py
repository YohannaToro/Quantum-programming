from calculadora import CalculadoraBasica

def suma_matrices(m1,m2):
    matriz=[[() for i in range(len(m1))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            matriz[i][j]=CalculadoraBasica.suma_complejos(m1[i][j],m2[i][j])        
    return matriz
def inversa_matrices(m1):
     matriz=[]
     for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append((m1[i][j][0]*-1,m1[i][j][1]*-1))
        matriz.append(vector)
     return matriz
def multiplicacion_complejas(m1,m2):
    matriz=[]
    for i in range(len(m1)):
        vector=[]        
        for j in range(len(m2[i])):
            suma=(0,0)
            for k in range (len(m2)):
                producto=CalculadoraBasica.producto_complejos(m1[i][k],m2[k][j])
                suma=CalculadoraBasica.suma_complejos(suma,producto)
            vector.append(suma)
        matriz.append(vector)

    return matriz
def multiplicacion_escalar_matrices(c1,m1):
    matriz=[[() for i in range(len(m1[0]))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            matriz[i][j]=CalculadoraBasica.producto_complejos(c1,m1[i][j])        
    return matriz
def transpuesta(m1):
    matriz=[[() for i in range(len(m1))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            matriz[i][j]=m1[j][i]        
    return matriz
  
def matriz_conjugada(m1):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j]=CalculadoraBasica.conjugado_complejos(m1[i][j])       
    return m1

def matriz_adjunt(m1):
    return matriz_conjugada(transpuesta(m1))
def multiplicacion_matrices(x,y):
    matriz=[[() for i in range(max(len(x[0]),len(y[0])))] for j in range(max(len(x),len(y)))]
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                matriz[i][j] +=CalculadoraBasica.producto_complejos(x[i][k],y[k][j])
    return matriz
def matriz_identidad(m1):
    matriz=[[() for i in range(len(m1[0]))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            if i==j:matriz[i][j]=(1,0)
            else: matriz[i][j]=(0,0)
    return matriz
def matriz_unitaria(m):
    return multiplicacion_matrices(matriz_adjunt(m),m)==matriz_identidad(m)
def matriz_hermiltan(m):
    return (m==matriz_adjunt(m))
def norma_matrices(m1):
    resultado=(0,0)
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            resultado=CalculadoraBasica.suma_complejos((CalculadoraBasica.producto_complejos(m1[i][j],CalculadoraBasica.conjugado_complejos(m1[i][j]))),resultado)
    return resultado[0]**0.5
def distancia_entre_matrices(m1,m2):
    resultado=(0,0)
    if(len(m1)-len(m2)!=0):
        return "las dimensiones deben ser iguales"
    else:
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                r1=CalculadoraBasica.resta_complejos(m1[i][j],m2[i][j])
                r2=CalculadoraBasica.resta_complejos(CalculadoraBasica.conjugado_complejos(m1[i][j]),CalculadoraBasica.conjugado_complejos(m2[i][j]))
                resultado=CalculadoraBasica.suma_complejos(CalculadoraBasica.producto_complejos(r1,r2),resultado)
        return resultado[0]**0.5

def producto_tensor(m1,m2):
    Matriz=[]
    for i in range(len(m1)):
        LaMatriz=[[]]*len(m2)
        for j in range(len(m1[i])):            
            m3=multiplicacion_escalar_matrices(m1[i][j],m2)
            for k in range(len(m2)):
                LaMatriz[k]=LaMatriz[k]+m3[k]
        for k in range(len(m2)):
            Matriz.append(LaMatriz[k])
        
    return Matriz
def transpuesta_vector(v1):
    matriz=[]
    for i in range(len(v1)):
        vector=[v1[i]]
        matriz.append(vector)
    return matriz
def adjunta_vector(m1):
    print(m1)
    M = [[(0,0) for j in range(len(m1))] for i in range(len(m1[0]))]
    print(M)
    for i in range(0,len(m1[0])):
        for j in range(0,len(m1)):
            print(m1[i][j])
            M[i][j]=m1[j][i]        

    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append((M[i][j][0],M[i][j][1]*-1))        
        matriz.append(vector)
    return matriz 
