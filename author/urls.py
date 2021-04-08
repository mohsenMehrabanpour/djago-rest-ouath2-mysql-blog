from django.urls import path
from author.views import profile,AuthorPosts
urlpatterns = [
    path('',profile.as_view(),name='profile_page'),
    path('posts/', AuthorPosts.as_view(), name='author_posts_page')
]
