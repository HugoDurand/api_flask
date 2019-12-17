from .. import db
from ..service.elastic_service import SearchableMixin

class Video(SearchableMixin, db.Model):
    """ Video Model """
    __tablename__ = 'video'
    __searchable__ = ['title']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(500), nullable=False)
    duration = db.Column(db.Float, nullable=False)
    post_date = db.Column(db.DateTime, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    comments = db.relationship("Comment", lazy="dynamic", cascade='all, delete-orphan', passive_deletes=True)
    
    def __repr__(self):
        return '<Video %r>' % self.title