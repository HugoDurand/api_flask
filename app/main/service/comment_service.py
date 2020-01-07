import datetime

from app.main import db
from app.main.model.comment import Comment

def new_comment(data):

    comment = Comment.query.filter_by(
        text=data['text'], 
        video_id = data['video_id']).first()

    if not comment:
        new_comment = Comment(
            text=data['text'],
            video_id=data['video_id'],
            post_date=datetime.datetime.utcnow()
        )
        db.session.add(new_comment)
        db.session.commit()

        response_object = {
            'status': 'success',
            'message': 'The comment as been posted',
        }
        return response_object, 201

    else:
        response_object = {
            'status': 'fail',
            'message': 'The comment already exists',
        }
        return response_object, 409


def get_comments():
    return Comment.query.all()

def get_comment(id):
    return Comment.query.filter_by(id=id).first()