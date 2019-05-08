from django.shortcuts import render,HttpResponse
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse 
from .forms import PostForm
from .models import Post

# Create your views here.

# def post(request):

#     return HttpResponse('POST picture')
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create.html'
    # success_url=reverse('list')


class PostList(ListView):
    model = Post 
    template_name = 'post_list.html'

class PostDetail(DetailView):
    model = Post
    template_name =  'post_detail.html'



    