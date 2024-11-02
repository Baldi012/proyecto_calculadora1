import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        """
        Se ejecuta antes de cada test
        Inicializa una nueva instancia de la calculadora
        """
        self.calc = Calculadora()

    def test_suma(self):
        """Pruebas para la función de suma"""
        # Casos normales
        self.assertEqual(self.calc.sumar(3, 5), 8)
        self.assertEqual(self.calc.sumar(-1, 1), 0)
        self.assertEqual(self.calc.sumar(0, 0), 0)
        
        # Números decimales
        self.assertAlmostEqual(self.calc.sumar(3.5, 2.5), 6.0)
        self.assertAlmostEqual(self.calc.sumar(-1.5, 1.5), 0.0)

    def test_resta(self):
        """Pruebas para la función de resta"""
        # Casos normales
        self.assertEqual(self.calc.restar(5, 3), 2)
        self.assertEqual(self.calc.restar(1, 1), 0)
        self.assertEqual(self.calc.restar(0, 0), 0)
        
        # Números negativos
        self.assertEqual(self.calc.restar(-5, -3), -2)
        
        # Números decimales
        self.assertAlmostEqual(self.calc.restar(5.5, 2.5), 3.0)

    def test_multiplicacion(self):
        """Pruebas para la función de multiplicación"""
        # Casos normales
        self.assertEqual(self.calc.multiplicar(3, 4), 12)
        self.assertEqual(self.calc.multiplicar(-2, 3), -6)
        self.assertEqual(self.calc.multiplicar(0, 5), 0)
        
        # Números decimales
        self.assertAlmostEqual(self.calc.multiplicar(2.5, 2), 5.0)
        
        # Multiplicación por cero
        self.assertEqual(self.calc.multiplicar(0, 0), 0)

    def test_division(self):
        """Pruebas para la función de división"""
        # Casos normales
        self.assertEqual(self.calc.dividir(6, 2), 3)
        self.assertEqual(self.calc.dividir(-6, 2), -3)
        self.assertAlmostEqual(self.calc.dividir(5, 2), 2.5)
        
        # División por cero
        self.assertEqual(self.calc.dividir(5, 0), "Error: No se puede dividir por cero.")
        
        # División de cero
        self.assertEqual(self.calc.dividir(0, 5), 0)

    def test_potencia(self):
        """Pruebas para la función de potencia"""
        # Casos normales
        self.assertEqual(self.calc.potencia(2, 3), 8)
        self.assertEqual(self.calc.potencia(2, 0), 1)
        self.assertEqual(self.calc.potencia(0, 5), 0)
        
        # Exponentes negativos
        self.assertAlmostEqual(self.calc.potencia(2, -2), 0.25)
        
        # Números decimales
        self.assertAlmostEqual(self.calc.potencia(2.5, 2), 6.25)

    def test_raiz_cuadrada(self):
        """Pruebas para la función de raíz cuadrada"""
        # Casos normales
        self.assertEqual(self.calc.raiz_cuadrada(4), 2)
        self.assertEqual(self.calc.raiz_cuadrada(0), 0)
        self.assertAlmostEqual(self.calc.raiz_cuadrada(2), 1.4142135623730951)
        
        # Números negativos
        self.assertEqual(
            self.calc.raiz_cuadrada(-4),
            "Error: No se puede calcular la raíz cuadrada de un número negativo"
        )

    def test_promedio(self):
        """Pruebas para la función de promedio"""
        # Casos normales
        self.assertEqual(self.calc.promedio(4, 6), 5)
        self.assertEqual(self.calc.promedio(-4, 6), 1)
        self.assertEqual(self.calc.promedio(0, 0), 0)
        
        # Números decimales
        self.assertAlmostEqual(self.calc.promedio(3.5, 7.5), 5.5)

    def test_porcentaje(self):
        """Pruebas para la función de porcentaje"""
        # Casos normales
        self.assertEqual(self.calc.porcentaje(50, 100), "50.0%")
        self.assertEqual(self.calc.porcentaje(25, 50), "50.0%")
        self.assertEqual(self.calc.porcentaje(0, 100), "0.0%")
        
        # Caso base cero
        self.assertEqual(
            self.calc.porcentaje(50, 0),
            "Error: No se puede calcular el porcentaje con base cero"
        )

    def test_historial(self):
        """Pruebas para el historial de operaciones"""
        # Realizar algunas operaciones
        self.calc.sumar(2, 3)
        self.calc.restar(5, 2)
        self.calc.multiplicar(4, 2)
        
        # Verificar que el historial tiene el número correcto de entradas
        self.assertEqual(len(self.calc.historial), 3)
        
        # Verificar que las entradas del historial son strings
        self.assertTrue(all(isinstance(entrada, str) for entrada in self.calc.historial))
        
        # Verificar que las operaciones se registran en el orden correcto
        self.assertTrue("suma" in self.calc.historial[0].lower())
        self.assertTrue("resta" in self.calc.historial[1].lower())
        self.assertTrue("multiplicación" in self.calc.historial[2].lower())

    def test_operaciones_diccionario(self):
        """Pruebas para verificar que todas las operaciones están en el diccionario"""
        operaciones_esperadas = {
            'suma', 'resta', 'multiplica', 'divide',
            'potencia', 'raiz', 'promedio', 'porcentaje'
        }
        self.assertEqual(
            set(self.calc.operaciones.keys()),
            operaciones_esperadas
        )

def run_tests():
    """Función para ejecutar todas las pruebas"""
    unittest.main(argv=[''], verbosity=2, exit=False)

if __name__ == '__main__':
    run_tests()