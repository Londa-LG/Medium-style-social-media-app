from django.shortcuts import render
from User.models import Posts

# Create your views here.

def homepage(request):
    return render(request,'main/home.html')

def blog_posts(request):
    post = Posts.objects.all()
    content = {'post': post}
    return render(request,'main/posts.html',content)