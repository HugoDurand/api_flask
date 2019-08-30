import datetime

from app.main import db
from app.main.model.video import Video


def new_video(data):

    video = Video.query.filter_by(
        title=data['title'], 
        duration=data['duration']).first()

    if not video:
        new_video = Video (
            title=data['title'],
            link=data['link'],
            duration=data['duration'],
            post_date=datetime.datetime.utcnow(),
            category_id=data['category_id']
        )
        db.session.add(new_video)
        db.session.commit()

        response_object = {
            'status': 'success',
            'message': 'The Video as been uploaded',
        }
        return response_object, 201

    else:
        response_object = {
            'status': 'fail',
            'message': 'The Video already exists',
        }
        return response_object, 409


def get_videos():
    return Video.query.all()


def get_video(id):
    return Video.query.filter_by(id=id).first()