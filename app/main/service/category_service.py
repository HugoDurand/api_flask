from app.main import db
from app.main.model.category import Category


def new_category(name):

    category = Category.query.filter_by(
        name=name).first()

    if not category:
        new_category = Category(
            name=name
        )
        db.session.add(new_category)
        db.session.commit()

        return new_category
    else:
        raise Exception('The Category already exists')


def get_categories():
    return Category.query.all()


def get_category(id):
    return Category.query.filter_by(id=id).first()
