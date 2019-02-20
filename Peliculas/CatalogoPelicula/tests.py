from django.test import TestCase
from .views import vista

from .views import vista
# Create your tests here.


class TestCatalogo(TestCase):
    """docstring for TestCatalogo"""

    def test_smoker(self):
        self.assertEquals(2, 1+1)

    def test_catalogo(self):
        self.assertFalse(False)

<<<<<<< HEAD
    def test_cuandoEsTrue(self):
        self.assertEquals('Es true', vista(True))

    def test_cuandoEsFalse(self):
        self.assertEquals('Es false', vista(False))
=======
    def test_cuando_es_true(self):
        self.assertEquals('Es True', vista(True))

    def test_cuando_es_false(self):
        self.assertEquals('Es False', vista(False))
>>>>>>> refs/remotes/origin/master
