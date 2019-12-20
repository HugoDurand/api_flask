from .. import db

association_table = db.Table('association', db.Model.metadata,
                             db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
                             db.Column('video_id', db.Integer, db.ForeignKey('video.id'))
                             )


class Category(db.Model):
    """ Category Model """
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            "name": self.name
        }

    def __repr__(self):
        return '<Category %r>' % self.name
