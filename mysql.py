'''
Arquivo de exemplo
'''

import pymysql
from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

db = pymysql.connect('localhost', 'root', 'root', 'teste')

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

USUARIOS = {
    'nilson':'123',
    'cunha':'321'
}

@auth.verify_password
def verificacao(login, senha):
    print('validando usuário')
    print(USUARIOS.get(login) == senha)
    if not (login, senha):
        return False
    return USUARIOS.get(login) == senha


class Pessoas(Resource):
    @auth.login_required
    def get(self, id):
        cursor = db.cursor()
        sql = 'SELECT * FROM pessoa WHERE id = %s'
        cursor.execute(sql, id)
        results = cursor.fetchall()
        return results


class Profissoes(Resource):

    def get(self):
        cursor = db.cursor()
        sql = 'SELECT * FROM profissao pf'
        cursor.execute(sql)
        results = cursor.fetchall()
        return [x for x in results]


api.add_resource(Pessoas, '/pessoas/<int:id>')
api.add_resource(Profissoes, '/profissao')

if __name__ == '__main__':
    app.run(debug=True)
