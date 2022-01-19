from app.extensions import db, Blueprint

user_api = Blueprint('user_api', __name__)

class User:
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    email = db.Column(db.String(60), unique=True, index=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String)
    favorites = db.Column(db.String)

    # Cria relacao com outras tabelas
    shopping_carts = db.relationship('shoppingCart')
    discount_coupons = db.relationship('discountCoupon')

    def json(self):
        return {
            "id":self.id,
            "name":self.name,
            "cpf":self.cpf,
            "email":self.email,
            "username":self.username,
            "password":self.password,
            "favorites":self.favorites
        }

