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


def usuario_login(matricula):
    conex = get_connection()
    cursor = conex.cursor()

    sql = """
    SELECT id, nome, sobrenome, email, senha_hash, cpf, matricula1, matricula2 
    FROM usuario 
    WHERE matricula1 = %s OR matricula2 = %s
    """

    cursor.execute(sql, (matricula, matricula))
    user = cursor.fetchone()

    cursor.close()
    conex.close()

    if not user:
        return None
    
    # converter para dicionário
    colunas = ["id", "nome", "sobrenome", "email", "senha", "cpf", "matricula1", "matricula2"]

    return dict(zip(colunas, user))

def criar_papel(nome):
    conex = get_connection()
    cursor = conex.cursor()

    sql = """
    INSERT INTO Papel (nome)
    VALUES (%s)
    """

    cursor.execute(sql, (nome, ))
    conex.commit()
    cursor.close()
    conex.close()


def usuario_existe(usuario_id):
    conex = get_connection()
    cursor = conex.cursor()

    sql = """
        SELECT id FROM usuario WHERE id = %s    
        """
    cursor.execute(sql, (usuario_id,))
    resultado = cursor.fetchone()

    cursor.close()
    conex.close()

    return resultado is not None


def placa_existe(placa):
    conex = get_connection()
    cursor = conex.cursor()

    sql = """
        SELECT id FROM veiculo WHERE PLACA = %s
        """
    cursor.execute(sql, (placa,))
    resultado = cursor.fetchone()

    cursor.close()
    conex.close()

    return resultado is not None


def criar_veiculo(usuario_id, placa):
    conex = get_connection()
    cursor = conex.cursor()

    sql = """
        INSERT INTO veiculo (usuario_id, placa)
        VALUES (%s, %s)
        """
    
    cursor.execute(sql, (usuario_id, placa))
    conex.commit()
    cursor.close()
    conex.close()


def criar_cancela(nome, tipo, status=None):
    conex = get_connection()
    cursor = conex.cursor()

    if status is None:
        sql = """
            INSERT INTO cancela (nome, tipo)
            VALUES (%s, %s)
            """
        params = (nome, tipo)

    else:
        sql = "INSERT INTO cancela (nome, tipo, status) VALUES (%s, %s, %s)"
        params = (nome, tipo, status)

    cursor.execute(sql, params)
    conex.commit()
    novo_id = cursor.lastrowid

    cursor.close()
    conex.close()


def alterar_tipo_cancela(id_cancela, novo_tipo):
    conex = get_connection()
    cursor = conex.cursor()

    sql = "UPDATE cancela SET tipo = %s WHERE ID = %s"
    cursor.execute(sql, (novo_tipo, id_cancela))
    conex.commit()
    atualizado = cursor.rowcount > 0

    cursor.close()
    conex.close()

    return atualizado