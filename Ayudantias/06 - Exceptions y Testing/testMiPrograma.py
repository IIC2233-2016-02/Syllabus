import unittest


class Creador:
    def __init__(self, attribute):
        self.attribute = attribute

    def change_attribute(self, new):
        'Recibe un parametro y setea attribute con ese parametro'
        self.attribute = new


class TestCreador(unittest.TestCase):
    def setUp(self):
        self.creator = Creador('Este es un string')

    def tearDown(self):
        del self.creator

    def test_change_attribute(self):
        self.assertIsInstance(self.creator.attribute, str)
        self.creator.change_attribute(11)
        self.assertIsInstance(self.creator.attribute, int)


suite = unittest.TestLoader().loadTestsFromTestCase(TestCreador)
unittest.TextTestRunner().run(suite)
