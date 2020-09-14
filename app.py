from flask import Flask
from flask_restful import Resource, Api
from models import connect, usuario
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# USUARIOS = {
#     'nilson':'321',
#     'cunha':'321'
# }

# @auth.verify_password
# def verificacao(login, senha):
#     if not (login, senha):
#         return False
#     return USUARIOS.get(login) == senha

@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return usuario(login=login, senha=senha)


class Pessoas(Resource):
    @auth.login_required
    def get(self):
        sql = 'select * from pessoa'
        conn = connect(sql)
        result = conn.fetchall()
        conn.close()
        return result


class Profissao(Resource):
    @auth.login_required
    def get(self):
        sql = 'select * from profissao'
        conn = connect(sql)
        result = conn.fetchall()
        conn.close()
        return [x for x in result]


api.add_resource(Pessoas, '/pessoas')
api.add_resource(Profissao, '/profissao')


if __name__ == '__main__':
    app.run(debug=True)
