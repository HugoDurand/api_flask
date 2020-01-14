import datetime

from app.main import db
from app.main.model.user import User


def new_user(email, password):
    user = User.query.filter_by(email=email).first()
    if not user:
        new_user = User(
            email=email,
            password=password,
            registered_on=datetime.datetime.utcnow()
        )
        db.session.add(new_user)
        db.session.commit()

        return generate_token(new_user)
    else:
        raise Exception('User already exists. Please Log in.')


def get_users():
    return User.query.all()


def get_user(id):
    return User.query.filter_by(id=id).first()


def generate_token(user):
    try:
        auth_token = user.encode_auth_token(user.id)
        return user, auth_token.decode()
    except Exception as e:
        raise e
