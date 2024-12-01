from django.shortcuts import render

def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    pass

def posts_details(request):
    pass