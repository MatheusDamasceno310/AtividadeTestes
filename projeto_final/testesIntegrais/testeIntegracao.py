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

class TestCadastro(unittest.TestCase):

    def test_conexao(self):
        formulario = {
            'usuario': 'admsupremo',
            'email': 'admsupremo@gmail.com',
            'telefone': '75 982892718',
            'senha': 'senhafraca',

        }

        conexao = requests.post('http://localhost:5000/cadastro', data=formulario)

        self.assertEqual(conexao.status_code, 200)

class TestGamezone(unittest.TestCase):

    def test_conexao(self):
        formulario = {
            'nomeCompleto': 'administrador',
            'emailRecado': 'admsupremo@gmail.com',
            'menssagem': 'teste'
        }

        conexao = requests.post('http://localhost:5000/gamezone', data=formulario)

        self.assertEqual(conexao.status_code, 200)

class TestUsuarios(unittest.TestCase):

    def test_conexao(self):

        conexao = requests.post('http://localhost:5000/usuarios')

        self.assertNotEqual(conexao.status_code, 200)

class TestCadastroJogos(unittest.TestCase):

    def test_conexao(self):

        conexao = requests.post('http://localhost:5000/cadastrar_jogos')

        self.assertEqual(conexao.status_code, 200)