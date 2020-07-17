from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import Post_Form, User_Registration

# Create your views here.
def user_profile(request):
    return render(request,'User/profile.html')

def user_registration(request):
    if request.method == "POST":
        form = User_Registration(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request,user)
            messages.success(request,f"{username} account created")
            return redirect("/blog/posts/")
        else:
            for msg in form.error_messages:
                messages.error(request,f"{msg}:{form.error_messages[msg]}")
    form = User_Registration()
    content = {'form':form}
    return render(request,'User/register.html',content)

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,'Login successful')
                return redirect("/blog/posts/")
            else:
                for msg in form.error_messages:
                    messages.error(request, f"{msg}:{form.error_messages[msg]}")
    form = AuthenticationForm()
    content = {'form': form }
    return render(request,'User/login.html',content)

def user_logout(request):
    logout(request)
    messages.info(request, 'Logout successful')
    return redirect("/")

def write_post(request):
    if request.method == "POST":
        form = Post_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Post created")
            return redirect("/")
    form = Post_Form()
    content = {'form': form }
    return render(request,'User/postw.html',content)