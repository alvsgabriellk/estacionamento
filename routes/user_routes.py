from flask import Blueprint, request, jsonify
from models.user_model import cadastro_usuario

# Blueprint chamado users
user_bp = Blueprint("users", __name__)

@user_bp.route("/cadastro", methods=["POST"])
def cadastro():
    dados = request.json

    nome = dados.get("nome")
    sobrenome = dados.get("sobrenome")
    email = dados.get("email")
    senha_hash = dados.get("senha_hash")
    cpf = dados.get("cpf")
    matricula = dados.get("matricula")

    #opcional
    #matricula2 = dados.get("matricula2")

    
    #todos dados obrigatórios
    if not all([nome, sobrenome, email, senha_hash, cpf, matricula]):
        return jsonify({"erro": "Preencha todos os campos obrigatórios."})
    
    # salvo no banco
    cadastro_usuario(nome, sobrenome, email, senha_hash, cpf, matricula)

    return jsonify({"msg": "Usuário cadastrado com sucesso!"}), 201
