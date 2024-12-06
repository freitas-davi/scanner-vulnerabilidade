# CRIANDO TABELAS DO BANCO DE DADOS

from . import db

class Tb_porta(db.Model):
    __tablename__ = 'Tb_porta'
    id = db.Column(db.Integer, primary_key = True)
    numero_porta = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(60), nullable=True)

    def __repr__(self):
        return f"<Tb_porta(id={self.id}, number='{self.numero_porta}')>"

