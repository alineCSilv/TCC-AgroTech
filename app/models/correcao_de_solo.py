from app.models import db

class CorrecaoDeSolo(db.Model):
    __tablename__ = 'correcao_de_solo'
    cod_correcao_de_solo = db.Column(db.Integer, primary_key=True)
    data_cadastro = db.Column(db.DateTime, default=db.func.current_timestamp())
    cod_usuario = db.Column(db.Integer, db.ForeignKey('usuario.cod_usuario'), nullable=False)
    cod_analise = db.Column(db.Integer, db.ForeignKey('analise_solo.cod_analise'), nullable=False)
    cod_cultura = db.Column(db.Integer, db.ForeignKey('culturas.cod_cultura'), nullable=False)
    gesso = db.Column(db.Float, nullable=False)
    cal = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<CorrecaoDeSolo {self.cod_correcao_de_solo}>'
