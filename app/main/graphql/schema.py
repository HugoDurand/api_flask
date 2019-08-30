import graphene
from ..model.video import Video
from ..model.comment import Comment
from ..model.user import User
from ..model.category import Category
from graphene_sqlalchemy import SQLAlchemyObjectType


class VideoObject(SQLAlchemyObjectType):
    class Meta:
        model = Video
        interfaces = (graphene.relay.Node, )


class CommentObject(SQLAlchemyObjectType):
    class Meta:
        model = Comment
        interfaces = (graphene.relay.Node, )


class CategoryObject(SQLAlchemyObjectType):
    class Meta:
        model = Category
        interfaces = (graphene.relay.Node, )


class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node, )
