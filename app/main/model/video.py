from .. import db
import datetime

class Video(db.Model):
    """ Video Model """
    __tablename__ = 'video'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(500), nullable=False)
    duration = db.Column(db.String(255), nullable=False)
    #duration = db.Column(db.Time, nullable=False)
    post_date = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return '<Post %r>' % self.title