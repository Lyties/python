from flask import Blueprint

sklean_route = Blueprint('sklean_study', __name__, url_prefix='/sklean')

from .views import *