from .. import db
import datetime

#TODO: find a way to pass by db instead of importing relationship from orm
from sqlalchemy.orm import relationship

class Video(db.Model):
    """ Video Model """
    __tablename__ = 'video'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(500), nullable=False)
    duration = db.Column(db.Time, nullable=False)
    post_date = db.Column(db.DateTime, nullable=False)

    def __init__(self):
        self.post_date = datetime.datetime.now()