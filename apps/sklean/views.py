from . import sklean_route as app
from flask import render_template

@app.route('/')
def index():
    return render_template('test.html')
