from flask import Flask, render_template
from apps.sklean import sklean_route

app = Flask(__name__)

app.register_blueprint(sklean_route)

@app.route('/')
def index():
    # return 'index';
    return render_template('index.html')


if __name__ == '__main__':
    app.run()