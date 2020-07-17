from django.shortcuts import render
from .models import Posts, Quotes


def homepage(request):
    post1 = Posts.objects.filter(id=1)
    post2 = Posts.objects.filter(id=2)
    post3 = Posts.objects.filter(id=3)
    comments = Quotes.objects.all()
    content= {"post1":post1, "post2":post2, "post3":post3, "comments": comments}
    return render(request,'main/home.html',content)

def blog_posts(request):
    post = Posts.objects.all()
    content = {'post': post}
    return render(request,'main/posts.html',content)

def post_view(request,id):
    post = Posts.objects.filter(id=id)
    content = {"post": post}
    return render(request,'main/post_view.html',content)