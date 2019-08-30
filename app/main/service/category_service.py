from app.main import db
from app.main.model.category import Category


def new_category(data):

    category = Category.query.filter_by(
        name=data['name']).first()

    if not category:
        new_category = Category(
            name=data['name']
        )
        db.session.add(new_category)
        db.session.commit()

        response_object = {
            'status': 'success',
            'message': 'The Category as been created',
        }
        return response_object, 201

    else:
        response_object = {
            'status': 'fail',
            'message': 'The Category already exists',
        }
        return response_object, 409


def get_categories():
    return Category.query.all()


def get_category(id):
    return Category.query.filter_by(id=id).first()
