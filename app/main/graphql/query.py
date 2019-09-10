import graphene
from .schema import VideoObject, CommentObject, UserObject, CategoryObject
from .mutations import Mutation
from ..model.video import Video
from ..model.comment import Comment
from ..model.user import User
from ..model.category import Category

class Query(graphene.ObjectType):
    videos = graphene.List(VideoObject)
    comments = graphene.List(CommentObject)
    users = graphene.List(UserObject)
    categories = graphene.List(CategoryObject)

    def resolve_videos(self, info, **kwargs):
        return Video.query.all()
    
    def resolve_comments(self, info, **kwargs):
        return Comment.query.all()

    def resolve_users(self, info, **kwargs):
        return User.query.all()

    def resolve_categories(self, info, **kwargs):
        return Category.query.all()

schema = graphene.Schema(query=Query, mutation=Mutation)