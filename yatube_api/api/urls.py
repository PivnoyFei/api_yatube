from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()

router.register('posts', PostViewSet, basename='index')
router.register('groups', GroupViewSet, basename='group')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment'
)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
