import graphene
from .schema import VideoObject, CommentObject, UserObject, CategoryObject
from .mutations import Mutation
from ..model.video import Video
from ..model.comment import Comment
from ..model.user import User
from ..model.category import Category

class Query(graphene.ObjectType):
    videos = graphene.List(VideoObject)
    video = graphene.Field(VideoObject, id=graphene.Int())

    comments = graphene.List(CommentObject)
    comment = graphene.Field(CommentObject, id=graphene.Int())

    users = graphene.List(UserObject)
    user = graphene.Field(UserObject, id=graphene.Int())

    categories = graphene.List(CategoryObject)
    category = graphene.Field(CategoryObject, id=graphene.Int())

    def resolve_videos(self, info, **kwargs):
        return Video.query.all()
    
    def resolve_video(root, info, id):
        return Video.query.filter_by(id=id).first()
    
    def resolve_comments(self, info, **kwargs):
        return Comment.query.all()
    
    def resolve_comment(root, info, id):
        return Comment.query.filter_by(id=id).first()

    def resolve_users(self, info, **kwargs):
        return User.query.all()
    
    def resolve_user(root, info, id):
        return User.query.filter_by(id=id).first()

    def resolve_categories(self, info, **kwargs):
        return Category.query.all()
    
    def resolve_category(root, info, id):
        return Category.query.filter_by(id=id).first()

schema = graphene.Schema(query=Query, mutation=Mutation)