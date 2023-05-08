import unittest
import requests
from bs4 import BeautifulSoup
from projeto_final.forms import FormCadastro

class TestCadastro(unittest.TestCase):

    def test_conexao(self):
        formulario = {
            'usuario': 'admsupremo',
            'email': 'admsupremo@gmail.com',
            'telefone': '75 982892718',
            'senha': 'senhafraca'
        }

        conexao = requests.post('http://localhost:5000/cadastro', data=formulario)

        self.assertEqual(conexao.status_code, 200)


