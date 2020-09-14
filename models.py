import pymysql

db = pymysql.connect('localhost', 'root', 'root', 'teste')


def connect(query, *args):
    conn = db.cursor()
    conn.execute(query, *args)
    return conn

def usuario(login, senha):
    sql = 'select login, senha ' \
          'from usuarios ' \
          'where login = %s and senha = %s'
    val = (login, senha)
    conn = connect(sql, val)
    result = conn.fetchone()
    conn.close()
    return result