import sys
import os
import unittest

from src.libro import Libro
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestLibro(unittest.TestCase):
    def setUp(self):
        self.libro = Libro("Cien años de soledad", 1967, "Gabriel García Márquez", 417)

    def test_titulo(self):
        self.assertEqual(self.libro.titulo, "Cien años de soledad")

    def test_anio_publicacion(self):
        self.assertEqual(self.libro.anio_publicacion, 1967)

    def test_autor(self):
        self.assertEqual(self.libro.autor, "Gabriel García Márquez")

    def test_num_paginas(self):
        self.assertEqual(self.libro.num_paginas, 417)


if __name__ == '__main__':
    unittest.main()
