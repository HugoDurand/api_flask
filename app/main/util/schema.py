import graphene
from ..model.video import Video
from ..model.comment import Comment
from ..model.user import User
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

class VideoObject(SQLAlchemyObjectType):
    class Meta:
        model = Video
        interfaces = (graphene.relay.Node, )

class CommentObject(SQLAlchemyObjectType):
    class Meta:
        model = Comment
        interfaces = (graphene.relay.Node, )

class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    videos = SQLAlchemyConnectionField(VideoObject)
    comments = SQLAlchemyConnectionField(CommentObject)
    users = SQLAlchemyConnectionField(UserObject)

schema = graphene.Schema(query=Query)
