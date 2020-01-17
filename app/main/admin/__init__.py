from flask_admin.contrib.sqla import ModelView

def create_admin(admin, db):

    from app.main.model.category import Category
    from app.main.model.user import User
    from app.main.model.video import Video

    admin.add_view(ModelView(Video, db.session))
    admin.add_view(ModelView(Category, db.session))
    admin.add_view(ModelView(User, db.session))
