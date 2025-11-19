from crud.database.connection import get_connection

def cadastro_usuario(nome, sobrenome, email, senha_hash, cpf, matricula):
    conex = get_connection()
    cursor = conex.cursor()

    sql = """
    INSERT INTO usuario (nome, sobrenome, email, senha_hash, cpf, matricula)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (nome, sobrenome, email, senha_hash, cpf, matricula))
    conex.commit()
    cursor.close()
    conex.close()