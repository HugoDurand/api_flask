import graphene

from .schema import VideoObject, CommentObject, CategoryObject, UserObject
from ..service.category_service import new_category
from ..service.comment_service import new_comment
from ..service.user_service import new_user
from ..service.video_service import new_video
from ..service.auth_service import Auth

from ..util.decorator import token_required, admin_token_required


class CreateVideo(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        link = graphene.String(required=True)
        duration = graphene.Int(required=True)
        categories = graphene.List(graphene.Int)

    video = graphene.Field(lambda: VideoObject)

    @admin_token_required
    def mutate(self, info, title, link, duration, categories):
        video = new_video(title, link, duration, categories)
        return CreateVideo(video=video)


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(lambda: CategoryObject)

    @admin_token_required
    def mutate(self, info, name):
        category = new_category(name)
        return CreateCategory(category=category)


class CreateComment(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)
        video_id = graphene.Int(required=True)

    comment = graphene.Field(lambda: CommentObject)

    @token_required
    def mutate(self, info, text, video_id):
        comment = new_comment(text, video_id)
        return CreateComment(comment=comment)


class CreateUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(lambda: UserObject)
    token = graphene.String()

    def mutate(self, info, email, password):
        user, token = new_user(email, password)
        return CreateUser(user=user, token=token)


class Login(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
    token = graphene.String()

    def mutate(self, info, email, password):
        token = Auth.login_user(email, password)
        return Login(token=token)


class Mutation(graphene.ObjectType):
    create_video = CreateVideo.Field()
    create_comment = CreateComment.Field()
    create_category = CreateCategory.Field()
    create_user = CreateUser.Field()
    login = Login.Field()
