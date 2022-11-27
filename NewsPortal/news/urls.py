from django.contrib import admin
from django.urls import path, include
from .views import PostsList, PostsDetail, SearchList, PostCreate, PostUpdate, PostDelete, CategoryListView, subscribe


urlpatterns = [
    # path('default/', default ),
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostsDetail.as_view(), name='post_detail'),
    path('search/', SearchList.as_view(), name='post_search'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name ='subscribe')
]
