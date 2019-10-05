from django.urls import path
from .views import (
    home,
    authors,
    published_post,
    create_post,
    post_detail,
    edit_post,
    saved_post,
    delete_post
)

urlpatterns = [
    path('',  home, name='home'),
    path('blog/',  home),
    path('blog/authors', authors, name='authors'),
    path('blog/create-post/', create_post, name='create_post'),
    path('blog/<str:username>/', published_post, name='published_post' ),
    path('blog/<str:username>/saved-post/', saved_post, name='saved_post' ),
    path('blog/<str:username>/<str:slug>/', post_detail, name='post_detail'),
    path('blog/<str:username>/<str:slug>/edit/', edit_post, name='edit_post'),
    path('blog/<str:username>/<str:slug>/delete/', delete_post, name='delete_post'),
    
    # path('<str:username>/<str:slug>/', views, 'post_detail'),
]
