from django.urls import path
from . import views,blog_view,comment_view,post_action_view



urlpatterns =  [
    path("", views.HomeView.as_view(),name="home"),
    path("about/",views.AboutView.as_view(),name="about"),
    path("blog-list/",views.ListBlogView.as_view(),name="blog-list"),
    path("blog/create/",blog_view.CreatePostView.as_view(),name="create-blog"),
    path("blog/details/<int:pk>/",blog_view.PostDetailView.as_view(),name="post_detail"),
    path("blog/details/<int:post_pk>/comments/add/",comment_view.CommentView.as_view(),name="add-comment"),
    path("blog/details/<int:pk>/delete/",blog_view.DeleteBlogView.as_view(),name="delete-post"),
    path("blog/details/<int:pk>/update/",blog_view.UpdatePostView.as_view(),name="update-post"),
    path("blog/details/<int:post_pk>/like/",post_action_view.LikeView.as_view(),name="like-post"),
    path("blog/details/<int:comment_pk>/comment/like/",post_action_view.CommentLikeView.as_view(),name="like-comment"),
  
]