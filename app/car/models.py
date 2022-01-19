from app.extensions import Blueprint
from app.models import Vehicle

car_api = Blueprint('car_api', __name__)

class Car(Vehicle):
    __tablename__ = "car"




