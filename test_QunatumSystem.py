import QuantumSystem as qs
import unittest

class TestClasicoCuamtico(unittest.TestCase):
     def test_transational_amplitude(self):

        result = qs.Transitional_amplitude([[((2**0.5/2),0),(0,(2**0.5/2))]],[[(0,(2**0.5/2)),(-(2**0.5/2),0)]])
        self.assertEqual(result,(0.0, -1.0))
     def test_specific_position(self):

        result = qs.probability_specific_position([(-3,-1),(0,-2),(0,1),(2,0)],2)
        self.assertEqual(result,0.052632)


if __name__ == '__main__':
    unittest.main()
