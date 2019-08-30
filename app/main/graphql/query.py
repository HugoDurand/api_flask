import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .schema import VideoObject, CommentObject, UserObject, CategoryObject
from .mutations import Mutation

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    videos = SQLAlchemyConnectionField(VideoObject)
    comments = SQLAlchemyConnectionField(CommentObject)
    users = SQLAlchemyConnectionField(UserObject)
    categories = SQLAlchemyConnectionField(CategoryObject)

schema = graphene.Schema(query=Query, mutation=Mutation)