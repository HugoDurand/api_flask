import datetime

from app.main import db
from app.main.model.comment import Comment

def new_comment(text, video_id):

    comment = Comment.query.filter_by(
        text=text,
        video_id = video_id).first()

    if not comment:
        new_comment = Comment(
            text=text,
            video_id=video_id,
            post_date=datetime.datetime.utcnow()
        )
        db.session.add(new_comment)
        db.session.commit()

        return new_comment

    else:
        raise Exception('The comment already exists')


def get_comments():
    return Comment.query.all()

def get_comment(id):
    return Comment.query.filter_by(id=id).first()