from django.shortcuts import render
from .models import Posts


def homepage(request):
    return render(request,'main/home.html')

def blog_posts(request):
    post = Posts.objects.all()
    content = {'post': post}
    return render(request,'main/posts.html',content)

def post_view(request,id):
    return render(request,'main/post_view.html')