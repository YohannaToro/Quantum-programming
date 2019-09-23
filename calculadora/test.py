import unittest
import CalculadoraBasica

class TestCalculadora(unittest.TestCase):
    def test_suma_complejos(self):
        """
        Este test retorna la suma entre un par de numeros complejos
        """
        result = CalculadoraBasica.suma_complejos((5,2),(-8,3))
        self.assertEqual(result, (-3,5))
    def test_resta_complejos(self):
        """
        Este test retorna la resta entre un par de numeros complejos
        """
        result = CalculadoraBasica.resta_complejos((5,2),(4,-2))
        self.assertEqual(result, (1,4))
    def test_producto_complejos(self):
        """
        Este test retorna el producto entre un par de numeros complejos
        """
        result = CalculadoraBasica.producto_complejos((1,2),(5,-2))
        self.assertEqual(result, (9,8))
    def test_division_complejos(self):
        """
        Este test retorna la sdivision entre un par de numeros complejos
        """
        result =CalculadoraBasica.division_complejos((5,-3),(2,1))
        self.assertEqual(result,(1.4, -2.2))
    def test_modulo_complejos(self):
        """
        Este test retorna el modulo de numeros complejos
        """
        result =CalculadoraBasica.modulo_complejos((8,-3))
        self.assertEqual(result,8.54400374531753)
    def test_polarCartesiano_complejos(self):
        """
        Este test retorna la suma entre un par de numeros complejos
        """
        result = CalculadoraBasica.conversion_polar_cartesiano(4,5)
        self.assertEqual(result, (3.984778792366982, 0.34862297099063266))
 
    def test_conjugado_complejos(self):
        """
        Este test retorna el conjugado de numeros complejos
        """
        result =CalculadoraBasica.conjugado_complejos((8,-12))
        self.assertEqual(result, (8, 12))
    def test_fase_complejos(self):
        """
        Este test retorna la fase de numeros complejos
        """
        result =CalculadoraBasica.fase_complejo((4,-3))
        self.assertEqual(result,-36.86989764584402)
    

if __name__ == '__main__':
    unittest.main()
