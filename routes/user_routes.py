from flask import Blueprint, request, jsonify
from models.user_model import cadastro_usuario, validar_matricula, usuario_login

# Blueprint chamado users
user_bp = Blueprint("users", __name__)
login_bp = Blueprint("login", __name__)

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
    dados = request.json
    matricula = dados.get('matricula')
    senha = dados.get('senha_hash')

    if not matricula or not senha:
        return jsonify({"erro": "Envie a matricula e senha!"}), 400
    
    usuario = usuario_login(matricula)
    if not usuario:
        return jsonify({"erro": "Matrícula não encontrada!"}), 400
    
    if usuario["senha"] != senha:
        return jsonify({"erro": "Senha incorreta!"}), 401
    
    return jsonify({"msg": "Login realizado com sucesso."}), 200


