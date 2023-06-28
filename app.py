from flask import Flask, render_template
from components.blueprint import registry
from components.db import initDB

app = Flask(__name__)
app.config.from_pyfile('conf/app.conf')
registry(app)
initDB(app)


@app.route('/')
def index():
    # return 'index';
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
