from django.urls import path, include
from post.api.views import PostList, PostDetail, PostCreate,CommentList, CommentCreate, CommentDetail

urlpatterns = [
    path('list/', PostList.as_view(), name='postlist'),
    path('create/', PostCreate.as_view(), name='postcreate'),
    path('<int:pk>/', PostDetail.as_view(), name='postdetail'),
    path('<int:pk>/commentlist/', CommentList.as_view(), name='commentlist'),
    path('<int:pk>/comment/', CommentCreate.as_view(), name='commentcreate'),
    path('comment/<int:pk>/', CommentDetail.as_view(), name='commentdetail')
]

