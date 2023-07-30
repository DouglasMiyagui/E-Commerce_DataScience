import unittest
from django.test import TestCase
from funcionarios.models import Funcionario

class FuncionarioTestCase(TestCase):
    def setUp(self):
        self.funcionario = Funcionario.objects.create(
            nome='John Doe',
            cargo='cientista_de_dados',
            nivel='pleno',
            salario=5000,
            data_contratacao='2022-01-01',
            ativo=True
        )

    def test_aumentar_salario(self):
        percentual = 10
        self.funcionario.aumentar_salario(percentual)
        self.assertEqual(self.funcionario.salario, 5500)

    def test_demitir(self):
        self.funcionario.demitir()
        self.assertFalse(self.funcionario.ativo)

    def test_str_representation(self):
        expected_str = 'John Doe'
        self.assertEqual(str(self.funcionario), expected_str)

if __name__ == '__main__':
    unittest.main()
