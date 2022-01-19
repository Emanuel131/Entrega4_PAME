from app.extensions import Blueprint
from app.models import Vehicle

motorcycle_api = Blueprint('motorcycle_api', __name__)

class Motorcycle(Vehicle):
    __tablename__ = "motorcycle"


