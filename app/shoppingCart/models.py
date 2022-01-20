from app.extensions import db, Blueprint

shopping_cart_api = Blueprint('shopping_cart_api', __name__)

class ShoppingCart(db.Model):
    __tablename__ = "shoppingCart"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    products = db.Column(db.PickleType)
    qnt_products = db.Column(db.Integer)
    price_before_coupon = db.Column(db.Float)
    price_final = db.Column(db.Float)
    used_coupon = db.Column(db.String)

    # Cria relacao com outras tabelas
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def json(self):
        return {
            "id":self.id,
            "products":self.products,
            "qnt_products":self.qnt_products,
            "price_before_coupon":self.price_before_coupon,
            "price_final":self.price_final,
            "used_coupon":self.used_coupon
        }

