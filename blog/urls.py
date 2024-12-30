from django.urls import path
from . import views

urlpatterns = [
    path("",views.StartingPageView.as_view(), name="starting-page"),
    path("posts/", views.AllPostsViews.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.PostDetails.as_view(), name="posts-details-page"), # for dynamic type content for better SEO /posts/my-posts
    path("read-later/", views.ReadLaterView.as_view(), name="read-later")
]
