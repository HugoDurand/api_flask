import graphene

from .mutations import Mutation
from .schema import VideoObject, CommentObject, UserObject, CategoryObject
from ..model.video import Video
from ..service.category_service import get_categories, get_category
from ..service.comment_service import get_comments, get_comment
from ..service.user_service import get_users, get_user
from ..service.video_service import get_videos, get_video


class Query(graphene.ObjectType):
    videos = graphene.List(VideoObject)
    video = graphene.Field(VideoObject, id=graphene.Int())

    search = graphene.List(VideoObject, value=graphene.String())

    comments = graphene.List(CommentObject)
    comment = graphene.Field(CommentObject, id=graphene.Int())

    users = graphene.List(UserObject)
    user = graphene.Field(UserObject, id=graphene.Int())

    categories = graphene.List(CategoryObject)
    category = graphene.Field(CategoryObject, id=graphene.Int())

    def resolve_videos(self, info, **kwargs):
        return get_videos()
    
    def resolve_video(root, info, id):
        return get_video(id)

    def resolve_search(self, info, value):
        return Video.search(value)
    
    def resolve_comments(self, info, **kwargs):
        return get_comments()

    def resolve_comment(root, info, id):
        return get_comment(id)

    def resolve_users(self, info, **kwargs):
        return get_users()
    
    def resolve_user(root, info, id):
        return get_user(id)

    def resolve_categories(self, info, **kwargs):
        return get_categories()
    
    def resolve_category(root, info, id):
        return get_category(id)

schema = graphene.Schema(query=Query, mutation=Mutation)