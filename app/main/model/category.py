from .. import db
from ..service.elastic_service import SearchableMixin


class Category(SearchableMixin, db.Model):
    """ Category Model """
    __tablename__ = 'category'
    __searchable__ = ['name']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    videos = db.relationship("Video", lazy="dynamic")

    def __repr__(self):
        return '<Category %r>' % self.name