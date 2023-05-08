import unittest
import requests

class TestLogin(unittest.TestCase):

    def test_conexao(self):
        formulario = {
            'usuario': 'admsupremo',
            'senha': 'senhafraca'
        }

        conexao = requests.post('http://localhost:5000/', data=formulario)

        self.assertEqual(conexao.status_code, 200)

