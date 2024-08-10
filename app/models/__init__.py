from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .usuario import Usuario
from .analise_solo import AnaliseSolo
from .culturas import Cultura
from .correcao_de_solo import CorrecaoDeSolo
