from components.db import db

class User(db.Model):
    
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), nullable=False)  # 用户姓名
    age = db.Column(db.Integer, nullable=False)  # 用户年龄
