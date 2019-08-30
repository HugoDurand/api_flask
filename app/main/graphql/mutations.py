import graphene
import datetime

from ..model.video import Video
from ..model.comment import Comment
from ..model.category import Category
from ..model.user import User

from .schema import VideoObject, CommentObject, CategoryObject

from app.main import db

class CreateVideo(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        link = graphene.String(required=True) 
        duration = graphene.Int(required=True)
        category_id = graphene.Int(required=True)

    video = graphene.Field(lambda: VideoObject)

    def mutate(self, info, title, link, duration, category_id):
        video = Video(title=title, link=link, duration=duration, post_date=datetime.datetime.utcnow(), category_id=category_id)
        db.session.add(video)
        db.session.commit()
        return CreateVideo(video=video)


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(lambda: CategoryObject)

    def mutate(self, info, name):
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
        return CreateCategory(category=category)


class CreateComment(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)
        video_id = graphene.Int(required=True)

    comment = graphene.Field(lambda: CommentObject)

    def mutate(self, info, text, video_id):
        comment = Comment(text=text, video_id=video_id, post_date=datetime.datetime.utcnow())
        db.session.add(comment)
        db.session.commit()
        return CreateComment(comment=comment)


class Mutation(graphene.ObjectType):
    create_video = CreateVideo.Field()
    create_comment = CreateComment.Field()
    create_category = CreateCategory.Field()
