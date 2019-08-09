import .. from db
import datetime

class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text, nullable=False)
    post_date = db.Column(db.DateTime, nullable=False)
    video_id = db.Column(db.Integer, ForeignKey('video.id'), nullable=False)

    def __init__(self):
        self.post_date = datetime.datetime.now()