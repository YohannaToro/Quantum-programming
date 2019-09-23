import math
def suma_complejos(c1,c2):
    return ((c1[0]+c2[0]),(c1[1]+c2[1]))
def resta_complejos(c1,c2):
    return ((c1[0]-c2[0]),(c1[1]-c2[1]))
def producto_complejos(c1,c2):
    real=(c1[0]*c2[0])-(c1[1]*c2[1])
    ima=(c1[0]*c2[1])+(c1[1]*c2[0])
    return ((real,ima))
def division_complejos(c1,c2):
     deno=producto_complejos(c2,(c2[0],(c2[1]*-1)))
     num=producto_complejos(c1,(c2[0],(c2[1]*-1)))
     return ((num[0]/deno[0]),(num[1]/deno[0]))
def modulo_complejos(c1):
    return ((c1[0]**2)+(c1[1]**2))**.5
def conjugado_complejos(c1):
    return (c1[0],(c1[1]*-1))
def conversion_polar_cartesiano(r,a):
    theta= math.radians(a)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x,y)
def fase_complejo(c1):
    theta=(c1[1]/c1[0])
    return ((math.degrees(math.atan(theta))))
