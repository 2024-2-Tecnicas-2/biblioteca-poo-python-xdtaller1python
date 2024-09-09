import sys
import os
import unittest
from io import StringIO

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
    
    def test_mostrar_info_libro(self):
        libro = Libro("Cien años de soledad", 1967, "Gabriel García Márquez", 417)
        with StringIO() as output:
            libro.mostrar_info(file=output)
            self.assertEqual(output.getvalue(), "Título: Cien años de soledad\nAño de publicación: 1967\nAutor: Gabriel García Márquez\nNúmero de páginas: 417\n")



if __name__ == '__main__':
    unittest.main()
