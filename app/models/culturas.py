from app.models import db

class Cultura(db.Model):
    __tablename__ = 'culturas'
    cod_cultura = db.Column(db.Integer, primary_key=True)
    cod_usuario = db.Column(db.Integer, db.ForeignKey('usuario.cod_usuario'), nullable=False)
    data_cadastro = db.Column(db.DateTime, default=db.func.current_timestamp())
    nome = db.Column(db.String(100), nullable=False)
    vl_saturacao_minima = db.Column(db.Float, nullable=False)
    vl_saturacao_recomendada = db.Column(db.Float, nullable=False)
    sg_estado = db.Column(db.String(2), nullable=False)

    def __repr__(self):
        return f'<Cultura {self.nome}>'
