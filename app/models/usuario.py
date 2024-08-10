from app.models import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuario'
    cod_usuario = db.Column(db.Integer, primary_key=True)
    data_cadastro = db.Column(db.DateTime, default=db.func.current_timestamp())
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(60), nullable=False)

    def set_password(self, password):
        #print(generate_password_hash(password))
        self.senha = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.senha, password)

    def __repr__(self):
        return f'<Usuario {self.nome}>'
