from rest_framework.routers import DefaultRouter

from apps.tags.views import TagAPIView
from apps.posts.views import PostAPIView, PostImageAPIView
from apps.comments.views import CommentAPIView
from apps.users.views import UserAPIView


router = DefaultRouter()

router.register(
    'posts',
    PostAPIView,
    basename='posts'
)
router.register(
    'posts-image',
    PostImageAPIView,
    basename='posts-image'
)
router.register(
    'tags',
    TagAPIView,
    basename='tags'
)
router.register(
    'comments',
    CommentAPIView,
    basename='comments'
)
router.register(
    'users',
    UserAPIView,
    basename='users'
)


urlpatterns = [

]

urlpatterns = router.urls
