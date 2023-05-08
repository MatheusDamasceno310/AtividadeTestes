import unittest
import requests

class TestCadastroJogos(unittest.TestCase):

    def test_conexao(self):

        conexao = requests.post('http://localhost:5000/cadastrar_jogos')

        self.assertEqual(conexao.status_code, 200)