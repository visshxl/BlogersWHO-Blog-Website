from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View
from .forms import CommentForm

from .models import Posts


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Posts
    ordering = ["-date", "title"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class AllPostsViews(ListView):
    template_name = "blog/all-posts.html"
    model = Posts
    ordering = ["-date", "title"]
    context_object_name = "all_posts"


class PostDetails(View):
    def isStoredPost(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, slug):
        post = Posts.objects.get(slug=slug)

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.isStoredPost(request, post.id)
        }
        return render(request, "blog/post-details.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Posts.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("posts-details-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.isStoredPost(request, post.id)
        }
        return render(request, "blog/post-details.html", context)


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        
        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Posts.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        
        return render(request, "blog/stored_posts.html", context)
            

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts= []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect("/")


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["post_tags"] = self.object.tags.all()
    #     context["comment_form"] = CommentForm()
    #     return context
    
# def posts_details(request, slug):
#     next_post = get_object_or_404(Posts, slug=slug)
#     return render(request, "blog/post-details.html",{
#         "post":next_post,
#         "post_tags":next_post.tags.all()
#     })


# def starting_page(request):
#     # sorted_posts=sorted(all_posts, key=get_date) 
#     # latest_posts= sorted_posts[-3:] # gives the 3 latest posts from the end
#     latest_posts = Posts.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html",{
#         "posts":latest_posts #passing the stored info to the template
#     })

# def posts(request): allpostsviews
#     return render(request, "blog/all-posts.html", {
#         "all_posts":Posts.objects.all()
#     })