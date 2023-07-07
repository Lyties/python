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
            dict = {
                'name': user.name,
                'age': user.age,
                'id': user.id
            }
            user_list.append(dict)

    return jsonify(code=200, message="OK", data={"users": user_list})

@app.route('save')
def save():
    u = User(name='qin',age=26)
    db.session.add(u)
    db.session.commit()
    return 'success'
