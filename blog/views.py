from django.shortcuts import render, get_object_or_404
from .models import Posts


def starting_page(request):
    # sorted_posts=sorted(all_posts, key=get_date) 
    # latest_posts= sorted_posts[-3:] # gives the 3 latest posts from the end
    latest_posts = Posts.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html",{
        "posts":latest_posts #passing the stored info to the template
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts":Posts.objects.all()
    })

def posts_details(request, slug):
    next_post = get_object_or_404(Posts, slug=slug)
    return render(request, "blog/post-details.html",{
        "post":next_post,
        "post_tags":next_post.tags.all()
    })