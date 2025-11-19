from flask import Flask
from routes.user_routes import user_bp, login_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(login_bp, url_prefix="/api")



if __name__ == "__main__":
    app.run(debug=True)