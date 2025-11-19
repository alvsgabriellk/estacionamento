from crud.database.connection import get_connection


def validar_matricula(codigo):
    conex = get_connection()
    cursor = conex.cursor()

    sql = "SELECT id FROM matriculas_validas where codigo = %s"
    cursor.execute(sql, (codigo,))
    existe = cursor.fetchone()

    cursor.close()
    conex.close()

    return existe is not None

def cadastro_usuario(nome, sobrenome, email, senha_hash, cpf, matricula1, matricula2=None):
    conex = get_connection()
    cursor = conex.cursor()

    sql = """
    INSERT INTO usuario (nome, sobrenome, email, senha_hash, cpf, matricula1, matricula2)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (nome, sobrenome, email, senha_hash, cpf, matricula1, matricula2))
    conex.commit()
    cursor.close()
    conex.close()