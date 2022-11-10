from django.contrib import admin
from django.urls import path, include
from .views import PostsList, PostsDetail


urlpatterns = [
    # path('default/', default ),
    path('', PostsList.as_view()),
    path('<int:pk>', PostsDetail.as_view()),
]
