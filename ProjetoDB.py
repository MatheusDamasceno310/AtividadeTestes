from projeto_final import banco, app

'''
Criar o banco de dados
'''
with app.app_context():
    banco.create_all()
