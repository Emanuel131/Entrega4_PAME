from app.extensions import db


# Classe para ser herdada por Carro e Moto
class Vehicle:
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(60))
    brand = db.Column(db.String(60))
    model = db.Column(db.String(60))
    manufacture_year = db.Column(db.Integer)
    isAvailable = db.Column(db.Boolean)
    price = db.Column(db.Float)
    kilometers_traveled = db.Column(db.Integer)
    accepted_fuel = db.Column(db.String)
    color = db.Column(db.String)
    optional_features = db.Column(db.String)
    gearshift_type = db.Column(db.String)
    engine_capacity = db.Column(db.String)
    photos = db.Column(db.String)   # Inserir path de imagem do veiculo
