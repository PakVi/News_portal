from django.contrib import admin
from django.urls import path, include
# from .views import PostsList, PostsDetail, SearchList, create_post, edit_post
# from .views import PostsList, PostsDetail, SearchList, PostCreate
from .views import PostsList, PostsDetail, SearchList, create_post, PostUpdate, PostDelete
from django.urls import reverse



urlpatterns = [
    # path('default/', default ),
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostsDetail.as_view(), name='post_detail'),
    path('search/', SearchList.as_view()),
    path('create/', create_post, name='create'),
    # path('create/', PostCreate.as_view(), name='product_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name ='post_edit'),
    # path('<int:pk>/edit/', edit_post, name ='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

]
