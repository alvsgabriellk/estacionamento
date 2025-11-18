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
    senha = dados.get("senha")
    cpf = dados.get("cpf")
    matricula1 = dados.get("matricula1")

    #opcional
    matricula2 = dados.get("matricula2")
