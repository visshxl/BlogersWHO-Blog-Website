from django.urls import path
from . import views

urlpatterns = [
    path("",views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.posts_details, name="posts-details-page") # for dynamic type content for better SEO /posts/my-posts
]
