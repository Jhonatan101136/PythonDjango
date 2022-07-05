import psycopg2
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = psycopg2.connect(host='localhost', database='agenda',
                              user='postgres', password='153')
    try:
        yield conexao
    finally:
        conexao.close()


def insert(nome, fone, email):
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql = 'INSERT INTO agenda (nome, fone, email) VALUES ' \
                  '(%s, %s, %s)'
            cursor.execute(sql, (nome, fone, email))
            conexao.commit()

# INSERE VÁRIOS REGISTROS NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO agenda (nome, fone, email) VALUES ' \
#               '(%s, %s, %s)'
#
#         dados = [
#             ('Lucas', '45988244844', 'lucas@rodrigues.gmail.com'),
#             ('Marcos', '45988235677', 'marcos@paulo.gmail.com'),
#             ('Elenilton', '459978-568', 'Elenilton@santos.gmail.com'),
#         ]
#
#         cursor.executemany(sql, dados)
#         conexao.commit()

# DELETA UM REGISTRO DA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM agenda WHERE id = %s'
#         cursor.execute(sql, (45988235677,))
#         conexao.commit()


# DELETA REGISTRA ENTRE UM RANGE
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM agenda WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (Marcos, Lucas))
#         conexao.commit()

# ATUALIZA UM REGISTRO NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'UPDATE agenda SET nome=%s, email=%s WHERE id=%s'
#         cursor.execute(sql, ('Pedro', 'pedro@sampaio.gmail.com', 5))
#         conexao.commit()

# INSERIR DADOS QUE SÃO SOLICITADOS AO USUÁRIO
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         nome = input('Informe seu nome: ')
#         fone = int(input('Informe seu número: '))
#         email = input('Informe seu email: '))
#
#         sql = 'INSERT INTO agenda (nome, fone, email) VALUES ' \
#               '(%s, %s, %s)'
#         cursor.execute(sql, (nome, fone, email))
#         conexao.commit()


