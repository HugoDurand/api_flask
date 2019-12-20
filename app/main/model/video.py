from .. import db
from ..service.elastic_service import SearchableMixin
from .category import association_table

class Video(SearchableMixin, db.Model):
    """ Video Model """
    __tablename__ = 'video'
    __searchable__ = ['title', 'categories']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(500), nullable=False)
    duration = db.Column(db.Float, nullable=False)
    post_date = db.Column(db.DateTime, nullable=False)
    categories = db.relationship("Category", secondary=association_table, backref="videos")
    comments = db.relationship("Comment", lazy="dynamic", cascade='all, delete-orphan', passive_deletes=True)

    def to_dict(self):
        return {
            "title": self.title,
            "categories": [category.to_dict() for category in self.categories],
        }
    
    def __repr__(self):
        return '<Video %r>' % self.title
