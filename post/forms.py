from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','cover','owner']
        # fields['owner']= request.user.id
        # fields = ['title','cover','owner']
    