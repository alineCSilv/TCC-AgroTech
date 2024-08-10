from app.models import db

class AnaliseSolo(db.Model):
    __tablename__ = 'analise_solo'
    cod_analise = db.Column(db.Integer, primary_key=True)
    data_cadastro = db.Column(db.DateTime, default=db.func.current_timestamp())
    cod_usuario = db.Column(db.Integer, db.ForeignKey('usuario.cod_usuario'), nullable=False)
    proprietario = db.Column(db.String(100), nullable=False)
    vl_ph = db.Column(db.Float, nullable=False)
    vl_fosforo = db.Column(db.Float, nullable=False)
    vl_potassio = db.Column(db.Float, nullable=False)
    vl_magnesio = db.Column(db.Float, nullable=False)
    vl_calcio = db.Column(db.Float, nullable=False)
    vl_h_al = db.Column(db.Float, nullable=False)
    vl_sb = db.Column(db.Float, nullable=False)
    vl_ctc = db.Column(db.Float, nullable=False)
    vl_saturacao = db.Column(db.Float, nullable=False)
    vl_im = db.Column(db.Float, nullable=False)
    vl_mo = db.Column(db.Float, nullable=False)
    vl_al = db.Column(db.Float, nullable=False)

    correcao_solos = db.relationship('CorrecaoDeSolo', backref='analise', lazy=True)

    def __repr__(self):
        return f'<AnaliseSolo {self.cod_analise}>'
