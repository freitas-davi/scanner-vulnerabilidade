import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'chave_secreta'

    # CONGIGURAÇÃO DO BANCO DE DADOS
    app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///flask_scanner.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

    # INICIALIZA O BANCO
    db.init_app(app)

    # Importar e registrar Blueprint
    from .routes import main
    app.register_blueprint(main)


    return app


