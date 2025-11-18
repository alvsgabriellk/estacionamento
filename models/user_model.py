from crud.database.connection import get_connection

def cadastro_usuario(nome, sobrenome, email, senha, cpf, matricula1, matricula2=None):
    conex = get_connection()
    cursor = conex.cursor()

    sql = """
    INSERT INTO usuarios (nome, sobrenome, email, senha, cpf, matricula1, matricula2)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (nome, sobrenome, email, senha, cpf, matricula1, matricula2))
    conex.commit()
    cursor.close()
    conex.close()