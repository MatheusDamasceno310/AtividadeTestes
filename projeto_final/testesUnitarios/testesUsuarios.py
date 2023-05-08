import unittest
import requests

class TestUsuarios(unittest.TestCase):

    def test_conexao(self):

        conexao = requests.post('http://localhost:5000/usuarios')

        self.assertNotEqual(conexao.status_code, 200)