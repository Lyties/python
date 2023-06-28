from flask import Blueprint

sklean_route = Blueprint('sklean_study',
                          __name__,
                            url_prefix='/sklean',
                            static_folder='static',
                            template_folder='templates')

from .views import *
