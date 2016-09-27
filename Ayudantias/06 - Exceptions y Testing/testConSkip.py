import unittest
import sys


def ejemplo():
    'Recuerda implementar este metodo!'
    pass


class TestCreador(unittest.TestCase):
    'Test que muestra un testeo normal, expectedFailures y los distintos skips'

    def setUp(self):
        self.elements = (1, 4, 2, 5, 11)

    def tearDown(self):
        del self.elements

    def test_in_tuple(self):  # Este es el unico que pasa correctamente
        self.assertIsInstance(self.elements, tuple)
        self.assertIn(1, self.elements)

    # Tenemos los mismos tests de antes, pero ahora con los skips y expected failure
    @unittest.skip('Aun no he implementado la funcion ejemplo()')
    def test_isnt_ready(self):
        print('Esto no se imprime porque se salto este test')
        self.assertTrue(ejemplo())

    @unittest.expectedFailure  # Sabemos que este siempre fallara
    def test_get_false(self):
        print('Aca si entra y falla, pero no lo marca como Failure sino que como x')
        self.assertFalse(True)

    @unittest.expectedFailure  # Que ocurre si decimos que fallara y no falla?
    def test_get_true(self):
        print('Como habiamos dicho que falla y no lo hizo, lo marca como u')
        self.assertTrue(True)

    @unittest.skipIf(sys.version_info.minor == 1, "no funciona en 3.1")
    def test_ignorar_if(self):
        print('Este python no es 3.1 asi que el test corre :)')
        self.assertEqual(False, True)

    @unittest.skipUnless(ejemplo() != None, "Solo funciona si ejemplo retorna algo")
    def test_ignorar_unless(self):
        print('solo entra cuando implementes el metodo ejemplo')
        self.assertEqual(ejemplo(), 'Ahora retorna!')


suite = unittest.TestLoader().loadTestsFromTestCase(TestCreador)
unittest.TextTestRunner().run(suite)
