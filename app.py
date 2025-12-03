from flask import Flask
from routes.user_routes import user_bp, login_bp, papel_bp, veiculo_bp, cancela_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(login_bp, url_prefix="/api")
app.register_blueprint(papel_bp, url_prefix="/papel")
app.register_blueprint(veiculo_bp, url_prefix="/veiculos")
app.register_blueprint(cancela_bp, url_prefix="/cancelas")




if __name__ == "__main__":
    app.run(debug=True)