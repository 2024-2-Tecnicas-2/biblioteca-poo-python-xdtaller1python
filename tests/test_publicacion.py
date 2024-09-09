import sys
import os
import unittest
from src.publicacion import Publicacion
from io import StringIO
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
    
    def test_mostrar_info_publicacion(self):
        publicacion = Publicacion("El Quijote", 1605)
        with StringIO() as output:
            publicacion.mostrar_info(file=output)
            self.assertEqual(output.getvalue(), "Título: El Quijote\nAño de publicación: 1605\n")

if __name__ == '__main__':
    unittest.main()
