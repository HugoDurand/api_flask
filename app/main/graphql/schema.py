import graphene
from ..model.video import Video
from ..model.comment import Comment
from ..model.user import User
from ..model.category import Category
from graphene_sqlalchemy import SQLAlchemyObjectType


class VideoObject(SQLAlchemyObjectType):
    class Meta:
        model = Video


class CommentObject(SQLAlchemyObjectType):
    class Meta:
        model = Comment


class CategoryObject(SQLAlchemyObjectType):
    class Meta:
        model = Category


class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
