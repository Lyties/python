from apps.sklean import sklean_route
from apps.user import user_route


def registry(app):
  app.register_blueprint(sklean_route)
  app.register_blueprint(user_route)
