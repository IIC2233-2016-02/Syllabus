import unittest
import os


class TestCompleto(unittest.TestCase):
    def setUp(self):
        # Se llama a setUo antes de cada test
        self.lista = [1, 2, 3, 4]
        archivo = open('ejemplo.txt', 'w')
        archivo.write('Esta es la primera linea')
        archivo.close()

    def tearDown(self):
        # Queremos que despues de nuestro testeo 'quede limpio'
        del self.lista
        os.remove('ejemplo.txt')

    def test_in_list(self):
        self.assertIn(1, self.lista)
        self.lista.append(8)
        self.assertIn(8, self.lista)

    def test_not_in_list(self):
        # ¿Esta el 8 que agregue antes?
        self.assertNotIn(8, self.lista)

    def test_in_file(self):
        file = open('ejemplo.txt', 'r')
        first = file.readline()
        file.close()
        self.assertEquals('Esta es la primera linea', first)


suite = unittest.TestLoader().loadTestsFromTestCase(TestCompleto)
unittest.TextTestRunner().run(suite)
