import sys
import os
import unittest
from io import StringIO
from src.revista import Revista
# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestRevista(unittest.TestCase):
    def setUp(self):
        self.revista = Revista("National Geographic", 2021, 150, "Exploración")

    def test_titulo(self):
        self.assertEqual(self.revista.titulo, "National Geographic")

    def test_anio_publicacion(self):
        self.assertEqual(self.revista.anio_publicacion, 2021)

    def test_numero(self):
        self.assertEqual(self.revista.numero, 150)

    def test_tema(self):
        self.assertEqual(self.revista.tema, "Exploración")
    
    def test_mostrar_info_revista(self):
        revista = Revista("National Geographic", 2021, 150, "Exploración")
        with StringIO() as output:
            revista.mostrar_info(file=output)
            self.assertEqual(output.getvalue(), "Título: National Geographic\nAño de publicación: 2021\nNúmero: 150\nTema: Exploración\n")

        
if __name__ == '__main__':
    unittest.main()
