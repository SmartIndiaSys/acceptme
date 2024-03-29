from project import db, login_manager
from flask_login import UserMixin
import sys
sys.path.append('../../')


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    insta_username = db.Column(db.String(100), unique=True, index=True)
    accept_request_count = db.Column(db.String, nullable=True)
    is_subscribed = db.Column(db.Boolean, default=False)
    subscription_plan = db.Column(db.String(100), nullable=True)
    from_date = db.Column(db.DateTime, nullable=True)
    till_date = db.Column(db.DateTime, nullable=True)

    def __init__(self, insta_username):
        self.insta_username = insta_username

    def is_authenticated(self):
        return True

    def __str__(self):
        return self.insta_username


class Counter(db.Model):
    __tablename__ = "counter"

    id = db.Column(db.Integer, primary_key=True)
    insta_username = db.Column(db.String(100), unique=True, index=True)
    counts = db.Column(db.Integer)

    def __init__(self, insta_username=None, counts=None):
        self.insta_username = insta_username
        self.counts = counts

    def __repr__(self):
        return '%r' % (self.counts)
