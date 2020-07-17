from django import forms
from main.models import Posts
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Post_Form(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            'post',
            'post_description',
            'post_title'
        ]
        widgets = {
            'post': forms.Textarea(attrs={"class":"materialize-textarea teal-text"}),
            'post_description': forms.TextInput(attrs={"type":"text", "class":"teal-text"}),
            'post_title': forms.TextInput(attrs={"type":"text","class":"teal-text"})
        }

class User_Registration(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        widgets = {
            'username': forms.TextInput(attrs={"type":"text"}),
            'email': forms.TextInput(attrs={"type":"text"}),
            'password1': forms.TextInput(attrs={"type": "text"}),
            'password2': forms.TextInput(attrs={"type": "text"}),
        }