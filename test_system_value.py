import sytemvla as sysv
import unittest

class TestSystemVal(unittest.TestCase):
     def test_probability_value(self):

        result = sysv.probability_specific_position([(-3,-1),(0,-2),(0,1),(2,0)],2)
        self.assertEqual(result,0.052632)

     def test_Transitional_amplitude(self):

        m=[[(1,0),(0,0),(0,0)],[(0,0),(0,0),(1/2,0)]]
        result = sysv.Transitional_amplitude([[((2**0.5/2),0),(0,(2**0.5/2))]],[[(0,(2**0.5/2)),(-(2**0.5/2),0)]])
        self.assertEqual(result,(0.0, -1.0))
        
     
     def test_experimento_canicas(self):
 
        m=[[(1,0),(0,0),(0,0)],[(0,0),(0,0),(1/2,0)]]
        result = sysv.half_value([[((2**0.5/2),0),(0,(2**0.5/2))]],[[(0,(2**0.5/2)),(-(2**0.5/2),0)]])
        self.assertEqual(result,(0.7071067811865477, 0.0))


if __name__ == '__main__':
    unittest.main()

