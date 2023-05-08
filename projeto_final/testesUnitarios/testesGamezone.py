import unittest
import requests

class TestGamezone(unittest.TestCase):

    def test_conexao(self):
        formulario = {
            'nomeCompleto': 'administrador',
            'emailRecado': 'admsupremo@gmail.com',
            'menssagem': 'teste'
        }

        conexao = requests.post('http://localhost:5000/gamezone', data=formulario)

        self.assertEqual(conexao.status_code, 200)