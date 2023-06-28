from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
def initDB(app):
  db.init_app(app=app)
  Migrate(app=app,db=db)
