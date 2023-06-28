from flask import Blueprint

user_route = Blueprint('user_study',
                          __name__,
                            url_prefix='/user',
                            static_folder='static',
                            template_folder='templates')
from .views import *
from components.db import db
