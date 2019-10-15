# Simulation program from classic to quantum


El sistema consiste en una partícula confinada a un conjunto discreto de posiciones en una línea. El simulador debe permitir especificar el número de posiciones y un vector ket de estado asignando las amplitudes.

## 1. CLASSICAL DETERMINISTIC SYSTEMS

simple system described by a graph as a Boolean adjacency matrix where M[i,j] = 1 if and only if there is an arrow from vertex j to vertex i .1 The requirement that every vertex has exactly one outgoing edge corresponds to the
fact that every column of the Boolean adjacency matrix contains exactly one 1. Also the system have a vertex state, so we multiply matrix (M) to state(x) of the system like the figure.

![Classical system](https://user-images.githubusercontent.com/37119524/66871685-ca879b00-ef69-11e9-9276-e79d49ee37b9.PNG)

```
The program should allow the user to enter a Boolean matrix that describes the
ways that marbles move. Make sure that the matrix follows our requirement. The user
should also be permitted to enter a starting state of how many marbles are on each
vertex. Then the user enters how many time clicks she wants to proceed. The computer
should then calculate and output the state of the system after those time clicks.
We will make changes to this program later in the chapter.
```
![Captura](https://user-images.githubusercontent.com/37119524/66871869-35d16d00-ef6a-11e9-8e19-357f1049dd8b.PNG)

## PROBABILISTIC SYSTEMS
We shall restrict our attention to weighted graphs that satisfy the following  conditions: 
The adjacency matrices for our graphs will have real entries between 0 and 1
where the sums of the rows and the sums of the columns are all 1
![Captura](https://user-images.githubusercontent.com/37119524/66872255-24d52b80-ef6b-11e9-9738-874cbb8e08a7.PNG)
```
Write a program that asks a user to design a multislit experiment. The user notes
the number of slits and the number of targets to measure the bullets. Then the user
enters probabilities of the bullets’ moving from each slit to each target. An appropriate
matrix is set up and then the matrix is multiplied by itself. Have the program print the
appropriate resulting matrix and vector.
```
![Captura](https://user-images.githubusercontent.com/37119524/66872366-6fef3e80-ef6b-11e9-80bd-29c437c321ae.PNG)
## QUANTUM SYSTEMS
The fact that complex numbers may cancel each other out when added has a
well-defined physical meaning in quantum mechanics (and in classical wave mechanics
as well). It is referred to as interference4 and it is one of the most important
concepts in quantum theory.
Let us generalize our states and graphs from the previous section. For our states,
rather than insisting that the sum of the entries in the column vector is 1, we shall
require that the sum of the modulus squared of the entries be 1.

1. The important point here is that the modulus squared is positive. For simplicity of calculation, we have
chosen easy complex numbers.
2. The clever reader might have considered something like “negative probability” to perform the same
task as complex numbers. It turns out that much of quantum mechanics can, in fact, be done that way.
However, it is not the standard way of introducing quantum theory, and we will not take that route.
3. We defined a “unitary matrix” in Section 2.6. Remember: A matrix U is unitary if U  U† = I =
U† x U.

![Captura](https://user-images.githubusercontent.com/37119524/66873452-176d7080-ef6e-11e9-945a-f768483ed2d0.PNG)

```
Modify your program from Programming Drill 3.2.2 so
that you allow transitions from the many slits to the many measuring devices to be
complex numbers. Your program should identify where there are interference phenomena.
```
![Captura](https://user-images.githubusercontent.com/37119524/66873595-661b0a80-ef6e-11e9-89ec-7a4040d6fd52.PNG)

## Lenguaje Programación


* Python
## Pre-requisaitos
* tener instalado python 3 o mayor
* Si no tiene instalado python siga el siguiente tutorial [https://es.wikihow.com/instalar-Python](https://es.wikihow.com/instalar-Python)
## Instalaciòn y ejecucion del proyecto
Descargue el repositorio lo puede realizar de dos formas descargando el .zip o usando git 

En caso de usar git la linea de comando para clonar el repositiorio es:

```
git clone https://github.com/YohannaToro/Quantum-programming.git
```

Abrir terminal y dirgirse a la carpeta calculadora

```
cd Quantum-programming
```
Ejecute el archivo con la siguiente linea de comando

```
python QuantumSystem.py
```

##  Ejecutar pruebas y aplicaciòn
Para ejecutar las pruebas es necesario ejecutar el archivo dirijase al archivo test.py que se encuentra en la raiz del proyecto.
	- abrir la consola de comando entrar a la carpeta raiz y poner la siguiente linea de comando
	
MacOs o Linux
	
		- python3 testClasico_Cuantico.py
	
Windows
		
		- python testClasico_Cuantico.py
		
		
Se corre un total de 14 pruebas correspondiente a cada una de las operaciones
