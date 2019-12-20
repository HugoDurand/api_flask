import datetime

from app.main import db
from app.main.model.video import Video
from app.main.model.category import Category


def new_video(data):

    video = Video.query.filter_by(
        title=data['title'], 
        duration=data['duration']).first()

    if not video:
        category = []
        for category_id in data['categories']:
            if category_id == 0:
                response_object = {
                    'status': 'fail',
                    'message': 'The Video doesn\'t have any category',
                }
                return response_object, 409

            search_category = Category.query.filter_by(id=category_id).first()

            if not search_category:
                response_object = {
                    'status': 'fail',
                    'message': 'The Video category doesn\'t exist',
                }
                return response_object, 409

            category.append(search_category)


        new_video = Video(
            title=data['title'],
            link=data['link'],
            duration=data['duration'],
            post_date=datetime.datetime.utcnow(),
            categories=category
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
