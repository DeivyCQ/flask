from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(70), index=True, unique=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password = db.Column(db.String(120))
    about_me = db.Column(db.String(180))
    last_time = db.Column(db.DateTime, default=datetime.now())
    posts = db.relationship('Post', backref='Author', lazy="dinamic")

    def __repr__(self):
        return f'User -> {self.username}'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def avatar():
        encoded = md5(self.email.lower().encode('UTF-8')).hexdigest()
        return f'https://es.gravatar.com/avatar/{encoded}?d=identicon&s={size}'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))