import datetime

from app.main import db
from app.main.model.video import Video
from app.main.model.category import Category



def new_video(title, link, duration, categories):

    video = Video.query.filter_by(
        title=title,
        duration=duration).first()

    if not video:
        category = []
        for category_id in categories:
            if category_id == 0:
                raise Exception('The Video doesn\'t have any category')
            search_category = Category.query.filter_by(id=category_id).first()

            if not search_category:
                raise Exception('The Video Category doen\'t exist')
            category.append(search_category)


        new_video = Video(
            title=title,
            link=link,
            duration=duration,
            post_date=datetime.datetime.utcnow(),
            categories=category
        )
        db.session.add(new_video)
        db.session.commit()

        return new_video
    else:
        raise Exception('The Video already exists')


def get_videos():
    return Video.query.all()


def get_video(id):
    return Video.query.filter_by(id=id).first()
