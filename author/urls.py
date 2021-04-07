from django.urls import path
from author.views import profile
urlpatterns = [
    path('',profile.as_view(),name='profile_page')
]
