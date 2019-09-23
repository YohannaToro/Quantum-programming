# Libreria con operaciones para matrices y vectores 


Los numeros comples es la suma entre un número real y uno de tipo **imaginario**  un número imaginario es aquél cuyo cuadrado es negativo.
La librería que soportar por lo menos las siguientes operaciones de matrices con números complejos:
Cada una de las funciones del programa recibe un par de matrices o una dependiendo de la función:

* Adición de vectores complejos.

* Inversa de vectores complejos.

* Multiplicación escalar de vectores complejos.

* Adición de matrices complejos.

* Inversa de matrices complejos.

* Multiplicación escalar de matrices complejas.

* Matriz transpuesta

* Matriz conjugada

* Matriz adjunta

* Función para calcular la "acción" de una matriz sobre un vector.

* Norma de matrices

* Distancia entrematrices

* Revisar si es unitaria

* Revisar si es Hermitian

* Producto tensor.
*PARAMETROS*

* m1,m2: matriz compuesta de numeros complejos (real,imaginario)	
ejemplo:
m1=[[(3,4),(1,2),(5,-1)],[(8,-1),(2,3),(4,7)],[(2,6),(5,3),(5,1)]]
m2=[[(1,5)],[(1,-4)],[(3,-1)]]

1.  Suma_matrices (m1,m2): 

		retorna la suma entre un par de martices de numeros complejos
2.  Inversa(m1): 

		retorna la matriz negativa

	
4.  Transpuesta(m1)

		retorna la transpuesta de la matriz 
5.   Conjugada (m1)

		retorna la matriz Conjugada
	
	
6.  Módulo(c1): 

		retorna el modulo de un número complejo.
	
7.  Conjugado(c1):

		retorna el conjugado de un numero complejo

8.  adjunta_matriz (m1): 

		retorna la matriz Adjunta


9. Accion(m1): 

		retorna la  accion de una matriz
		
10. norma(m1): 

		retorna la Norma de la matriz como un flotante
		
11. Distancia(m1,m2): 

		retorna la distancia entre un par de matrizes
12. Unitario(m1): 

		retorna un Booleano dependiende de si la matriz es unitaria o no
13. Hermitian(m1): 

		retorna un Booleano dependiende de si la matriz es Hermitian o no
14. ProductoTensor(m,m1): 

		retorna el punto Tensor que es una nueva Matriz


## Lenguaje Programación
* Python
## Pre-requisaitos
* tener instalado python 3 o mayor
* Si no tiene instalado python siga el siguiente tutorial [https://es.wikihow.com/instalar-Python](https://es.wikihow.com/instalar-Python)
## Instalaciòn y ejecucion del proyecto
Descargue el repositorio lo puede realizar de dos formas descargando el .zip o usando git 

En caso de usar git la linea de comando para clonar el repositiorio es:

```
git clone https://github.com/YohannaToro/Calculadora-Matrices.git
```

Abrir terminal y dirgirse a la carpeta calculadora

```
\Calculadora-Matrices
```
Ejecute el archivo con la siguiente linea de comando

```
python libreriaMatrices.py
```

##  Ejecutar pruebas y aplicaciòn
Para ejecutar las pruebas es necesario ejecutar el archivo dirijase al archivo test.py que se encuentra en la raiz del proyecto.
	- abrir la consola de comando entrar a la carpeta raiz y poner la siguiente linea de comando
	
MacOs o Linux
	
		- python3 test.py
	
Windows
		
		- python test.py
Se corre un total de 14 pruebas correspondiente a cada una de las operaciones
