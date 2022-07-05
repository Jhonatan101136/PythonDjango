import dados


def main():
    nome = str(input('Digite seu nome'))
    fone = int(input('Digite seu número'))
    email = str(input('Digite seu email'))


    # with dados.conecta() as conexao:
    #     with conexao.cursor() as cursor:
    #         nome = input('Informe seu nome: ')
    #         fone = int(input('Informe seu número: '))
    #         email = input('Informe seu email: ')

    # dados.insert(nome, fone, email)


    # with dados.conecta() as conexao:
    #     with conexao.cursor() as cursor:
    #         sql = 'DELETE FROM agenda WHERE id = %s'
    #         cursor.execute(sql, (457878,))
    #         conexao.commit()


    # with dados.conecta() as conexao:
    #     with conexao.cursor() as cursor:
    #         sql = 'UPDATE agenda SET nome=%s, email=%s WHERE id=%s'
    #         cursor.execute(sql, ('Pedro', 'pedro@sampaio.gmail.com', 5))
    #         conexao.commit()



main()

