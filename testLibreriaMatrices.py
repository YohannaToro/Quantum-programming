import libreriaMatrices
import unittest

m1=[[(7,3),(1,2),(5,-1)],[(-2,-1),(-7,-9),(-1,0)],[(3,8),(4,3),(2,1)]]
m2=[[(1,2),(1,2),(4,-1)],[(-2,-1),(-7,-9),(-1,0)],[(4,8),(4,3),(2,1)]]
class TestCalculadoraMatrices(unittest.TestCase):
    def test_caso_inversaVector(self):
        self.assertEqual([[(-3, -2), (-4, 2)]],libreriaMatrices.inversa_matrices([[[3,2],[4,-2]]]))
        """
        Este test retorna un vector
        """
        
    def test_suma_matrices(self):
        """
        Este test retorna la suma entre un par de numeros complejos
        """
        result = libreriaMatrices.suma_matrices([[[3,7],[5,-2]],[[1,8],[13,2]]],[[[-5,-6],[-9,2]],[[2,5],[-12,-9]]])
        self.assertEqual(result, [[(-2, 1), (-4, 0)], [(3, 13), (1, -7)]])
    def test_sMultiplicacionEscala_matrices(self):
        """
        Este test retorna la multiplicacion escalar entre una matriz y un numero complejo
        """
        result = libreriaMatrices.multiplicacion_escalar_matrices((3,1),[[(13,2),(1,0),(4,8)]])
        self.assertEqual(result,[[(37, 19), (3, 1), (4, 28)]] )
    def test_inversa_matrices(self):
        """
        Este test retorna la inversa de una matriz
        """
        result = libreriaMatrices.inversa_matrices(m1)
        self.assertEqual(result,[[(-7, -3), (-1, -2), (-5, 1)], [(2, 1), (7, 9), (1, 0)], [(-3, -8), (-4, -3), (-2, -1)]])
    def test_transpuesta_matrices(self):
        """
        Este test retorna la transpuesta de una matriz
        """
        result = libreriaMatrices.transpuesta(m2)
        self.assertEqual(result,[[(1, 2), (-2, -1), (4, 8)], [(1, 2), (-7, -9), (4, 3)], [(4, -1), (-1, 0), (2, 1)]])
   
    def test_matriz_conjugada(self):
        """
        Este test retorna una matriz conjugada
        """
        result = libreriaMatrices.matriz_conjugada(m1)
        self.assertEqual(result, [[(7, -3), (1, -2), (5, 1)], [(-2, 1), (-7, 9), (-1, 0)], [(3, -8), (4, -3), (2, -1)]])
    def test_matriz_adjunt(self):
        """
        Este test retorna la adjunta de una matriz
        """
        result = libreriaMatrices.matriz_adjunt(m2)
        self.assertEqual(result,[[(1, -2), (-2, 1), (4, -8)], [(1, -2), (-7, 9), (4, -3)], [(4, 1), (-1, 0), (2, -1)]] )
   
    def test_matriz_identidad(self):
        """
        Este test retorna la matriz identidad de una matriz
        """
        result = libreriaMatrices.matriz_identidad(m2)
        self.assertEqual(result, [[(1, 0), (0, 0), (0, 0)], [(0, 0), (1, 0), (0, 0)], [(0, 0), (0, 0), (1, 0)]])
    def test_matriz_unitaria(self):
        """
        Este test retorna una matriz unitaria
        """
        result = libreriaMatrices.matriz_unitaria([[(1,0),(0,0),(0,0)],[(0,0),(0,0),(1,0)],[(0,0),(1,0),(0,0)]])
        self.assertEqual(result,False)
   
    def test_norma_matrices(self):
        """
        Este test retorna la norma de una matrices
        """
        result = libreriaMatrices.norma_matrices(m1)
        self.assertEqual(result, 18.110770276274835)
    def test_distancia_matricesa(self):
        """
        Este test retorna la distancia entre los valores de un par de matrices
        """
        result = libreriaMatrices.distancia_entre_matrices(m1,m2)
        self.assertEqual(result,6.244997998398398 )
    def test_producto_tensor(self):
        """
        Este test retorna el producto tensor entre un par de matrices
        """
        result = libreriaMatrices.producto_tensor(m1,m2)
        self.assertEqual(result,[[(13, 11), (13, 11), (25, -19), (5, 0), (5, 0), (2, -9), (3, 11), (3, 11), (21, -1)], [(-17, -1), (-76, -42), (-7, 3), (-4, 3), (-25, 5), (-1, 2), (-9, -7), (-26, -52), (-5, -1)], [(52, 44), (37, 9), (17, 1), (20, 0), (10, -5), (4, -3), (12, 44), (17, 19), (9, 7)], [(-4, -3), (-4, -3), (-7, 6), (-25, -5), (-25, -5), (-19, 43), (-1, -2), (-1, -2), (-4, 1)], [(5, 0), (23, 11), (2, -1), (23, -11), (130, 0), (7, -9), (2, 1), (7, 9), (1, 0)], [(-16, -12), (-11, -2), (-5, 0), (-100, -20), (-55, 15), (-23, 11), (-4, -8), (-4, -3), (-2, -1)], [(19, -2), (19, -2), (4, -35), (10, 5), (10, 5), (13, -16), (4, 3), (4, 3), (7, -6)], [(-14, 13), (-93, 29), (-3, 8), (-11, 2), (-55, -15), (-4, 3), (-5, 0), (-23, -11), (-2, 1)], [(76, -8), (36, -23), (14, -13), (40, 20), (25, 0), (11, -2), (16, 12), (11, 2), (5, 0)]] )
        
    def test_matriz_hermiltan(self):
        """
        Este test retorna una matriz hermitan
        """
        result = libreriaMatrices.matriz_hermiltan(m2)
        self.assertEqual(result,False )
    def test_matriz_hermiltan(self):
        """
        Este test retorna una matriz hermitan
        """
        result = libreriaMatrices.matriz_hermiltan([[(5,0),(4,5),(6,-16)],[(4,-5),(13,0),(7,0)],[(6,16),(7,0),(-2.1,0)]])
        self.assertEqual(result,True )
    def test_caso_sumaVector(self):
        self.assertEqual([[(8, -4)]],libreriaMatrices.suma_matrices([[[3,2],[4,-2]]],[[[5,-6],[7,2]]]))
        """
        Este test retorna un vector
        """
        
    def test_multiplicacion_matrices(self):
        """
        Este test retorna la multiplicacion entre un par de matrices
        """
        result = libreriaMatrices.multiplicacion_matrices(m2,m2)
        self.assertEqual(result,[[(-3, 4, 0, -5, 24, 28), (-3, 4, 11, -23, 19, 8), (6, 7, -1, -2, 9, 2)], [(0, -5, 5, 25, -4, -8), (0, -5, -32, 126, -4, -3), (-9, -2, 7, 9, -2, -1)], [(-12, 16, -5, -10, 0, 20), (-12, 16, -1, -57, 5, 10), (24, 28, -4, -3, 3, 4)]])  

if __name__ == '__main__':
    unittest.main()

