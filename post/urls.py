from django.urls import path
from post.views import listPosts, Redirect_to_ListPosts

urlpatterns = [
    path('', Redirect_to_ListPosts.as_view(), name='redirect_to_list_posts'),
    path('posts/', listPosts.as_view(), name='list_posts')
]
