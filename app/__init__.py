from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'

    db.init_app(app)
    jwt.init_app(app)

    @app.route("/")
    def home():
        return jsonify({
            "status": "success",
            "message": "API is running"
        })

    return app