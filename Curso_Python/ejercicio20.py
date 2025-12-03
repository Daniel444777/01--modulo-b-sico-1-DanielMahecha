# ejercicio20.py - Unit Testing
import unittest

def sumar(a, b):
    return a + b

class PruebasUnitarias(unittest.TestCase):
    
    def test_suma_correcta(self):
        self.assertEqual(sumar(2, 3), 5)
        
    def test_suma_negativos(self):
        self.assertEqual(sumar(-1, 1), 0)

if __name__ == '__main__':
    print("Ejecutando pruebas...")
    unittest.main()