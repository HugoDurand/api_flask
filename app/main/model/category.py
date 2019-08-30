from .. import db


class Category(db.Model):
    """ Category Model """
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    videos = db.relationship("Video", lazy="dynamic")

    def __repr__(self):
        return '<Category %r>' % self.name