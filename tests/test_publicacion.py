import sys
import os
import unittest
from src.publicacion import Publicacion
# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestPublicacion(unittest.TestCase):
    def setUp(self):
        self.publicacion = Publicacion("El Quijote", 1605)

    def test_titulo(self):
        self.assertEqual(self.publicacion.titulo, "El Quijote")

    def test_anio_publicacion(self):
        self.assertEqual(self.publicacion.anio_publicacion, 1605)

    def test_anio_publicacion_negativo(self):
        with self.assertRaises(ValueError):
            Publicacion("Libro del futuro", -2023)

    def test_titulo_vacio(self):
        with self.assertRaises(ValueError):
            Publicacion("", 2023)
        
if __name__ == '__main__':
    unittest.main()
