from flask import Blueprint, request, jsonify
from models.user_model import cadastro_usuario, validar_matricula, usuario_login, criar_papel, usuario_existe, placa_existe, criar_veiculo, criar_cancela, alterar_tipo_cancela

# Blueprint chamado users
user_bp = Blueprint("users", __name__)
login_bp = Blueprint("login", __name__)
papel_bp = Blueprint("papel", __name__)
veiculo_bp = Blueprint("veiculo", __name__)
cancela_bp = Blueprint("cancela", __name__)




@user_bp.route("/cadastro", methods=["POST"])
def cadastro():
    dados = request.json

    nome = dados.get("nome")
    sobrenome = dados.get("sobrenome")
    email = dados.get("email")
    senha_hash = dados.get("senha_hash")
    cpf = dados.get("cpf")
    matricula1 = dados.get("matricula1")

    #opcional
    matricula2 = dados.get("matricula2")

    
    #todos dados obrigatórios
    if not all([nome, sobrenome, email, senha_hash, cpf, matricula1]):
        return jsonify({"erro": "Preencha todos os campos obrigatórios."}), 400
    

    if not validar_matricula(matricula1):
        return jsonify({"erro": "A matrícula principal não existe na faculdade."}), 400
    
    if matricula2:
        if not validar_matricula(matricula2):
            return jsonify({"erro": "A segunda matrícula é inválida."}), 400
    
    # salvo no banco
    cadastro_usuario(nome, sobrenome, email, senha_hash, cpf, matricula1, matricula2)

    return jsonify({"msg": "Usuário cadastrado com sucesso!"}), 201




@login_bp.route("/login", methods=["POST"])
def login():
    dados = request.get_json()
    matricula = dados.get('matricula')
    senha = dados.get('senha')

    if not matricula or not senha:
        return jsonify({"erro": "Envie a matricula e senha!"}), 400
    
    usuario = usuario_login(matricula)

    # garante que usuario é válido
    if not usuario:
        return jsonify({"erro": "Matrícula não encontrada!"}), 400
    
    if "senha" not in usuario:
        return jsonify({"erro": "Erro interno: senha não retornada pelo banco!"}), 500
    
    if usuario["senha"] != senha:
        return jsonify({"erro": "Senha incorreta!"}), 401
    
    return jsonify({"msg": "Login realizado com sucesso."}), 200


@papel_bp.route("/papel", methods=["POST"])
def cadastrar_papel():
    dados = request.get_json()
    nome = dados.get("nome")

    if not nome:
        return jsonify({"erro": "O nome do papl é obrigatório!"}), 400

    criar_papel(nome)

    return jsonify({"msg": "Papel criado com sucesso!"}), 201


@veiculo_bp.route("/veiculo", methods=["POST"])
def cadastrar_veiculo():
    dados = request.get_json()

    usuario_id = dados.get("usuario_id")
    placa = dados.get("placa")

    if not usuario_id or not placa:
        return jsonify({"erro": "Envie usuario_id e placa"}), 400
    
    if not usuario_existe(usuario_id):
        return jsonify({"erro": "Usuário não encontrado"}), 400
    
    if placa_existe(placa):
        return jsonify({"erro": "Placa já cadastrada!"}), 400
    
    criar_veiculo(usuario_id, placa)

    return jsonify({"msg": "Veículo cadastrado com sucesso!"}), 201




@cancela_bp.route("/cadastrar", methods=["POST"])
def cadastrar_cancela():
    dados = request.get_json() or {}

    nome = dados.get("nome")
    tipo = dados.get("tipo")
    status = dados.get("status")

    if not nome or not tipo:
        return jsonify({"erro": "Envie 'nome' e 'tipo'."}), 400
    
    if tipo not in ["ENTRADA", "SAIDA"]:
        return jsonify({"erro": "Tipo inválido. Use 'ENTRADA' ou 'SAIDA."}), 400
    
    novo_id = criar_cancela(nome, tipo, status)
    return jsonify({"msg": "Registro criado", "id": novo_id}), 201

@cancela_bp.route("/alterar_tipo/<int:id_cancela>", methods=["PUT"])
def alterar_tipo(id_cancela):
    dados = request.get_json() or {}
    novo_tipo = dados.get("tipo")

    if not novo_tipo:
        return jsonify({"erro": "Envie o campo 'tipo' (ENTRADA ou SAIDA)."}), 400
    
    if novo_tipo not in ["ENTRADA", "SAIDA"]:
        return jsonify({"erro": "Tipo inválido. Use 'ENTRADA' ou 'SAIDA'."}), 400
    
    sucesso = alterar_tipo_cancela(id_cancela, novo_tipo)
    if not sucesso:
        return jsonify({"erro": "Registro não encontrado."}), 404
    
    return jsonify({"msg": "Tipo atualizado com sucesso"}), 200





