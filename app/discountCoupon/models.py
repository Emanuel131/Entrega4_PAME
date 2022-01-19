from app.extensions import db, Blueprint

discount_coupon_api = Blueprint('discount_coupon_api', __name__)

class DiscountCoupon:
    __tablename__ = "discountCoupon"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isValid = db.Column(db.Boolean)
    promotion_name = db.Column(db.String(50))
    discount_value = db.Column(db.String(10))
    valid_through = db.Column(db.String(15))
    accepted_payment_method = db.Column(db.String(50))

    def json(self):
        return {
            "id":self.id,
            "isValid":self.isValid,
            "promotion_name":self.promotion_name,
            "discount_value":self.discount_value,
            "valid_through":self.valid_through,
            "accepted_payment_method":self.accepted_payment_method,
        }