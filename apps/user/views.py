from . import user_route as app
from components.db import db
from .models import User
from flask import jsonify
import json

@app.route('')
def users():
    users =  db.session.query(User).all()
    user_list = []
    if users:
        for user in users:
            user_list.append(str(user.__dict__))

    return jsonify(errno=200, errmsg="OK", data={"users": user_list})


def save():
    u = User(name='qin',age=26)
    db.session.add(u)
    db.session.commit()
    return 'success'
