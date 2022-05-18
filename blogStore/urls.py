from django.urls import path
from blogStore import views
from .views import DeleteBlog, Home, Article,AddPost, likeView, Edit


urlpatterns = [

    path('', Home.as_view(), name='home'),
    path('article/<int:pk>', Article.as_view(), name='article'),
    path('addpost/', AddPost.as_view(), name="addPost"),
    path('like/<int:pk>', likeView, name='like_post'),
    path('blog/edit/<int:pk>', Edit.as_view(), name="edit_blog"),
    path('blog/delete/<int:pk>', DeleteBlog.as_view(), name="delete_blog"),
]

