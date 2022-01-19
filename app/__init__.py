from app.extensions import db, Flask, migrate
from app.config import Config

# Importa blueprints
from app.user.models import user_api
from app.shoppingCart.models import shopping_cart_api
from app.discountCoupon.models import discount_coupon_api
from app.motorcycle.models import motorcycle_api
from app.car.models import car_api

# Cria app
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Registra blueprints
    app.register_blueprint(user_api)
    app.register_blueprint(shopping_cart_api)
    app.register_blueprint(discount_coupon_api)
    app.register_blueprint(motorcycle_api)
    app.register_blueprint(car_api)

    return app

