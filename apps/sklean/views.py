from . import sklean_route as app

@app.route('/')
def index():
    return 'test'