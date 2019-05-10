from django.shortcuts import render,HttpResponse
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy 
from .forms import PostForm
from .models import Post
from django.contrib.auth.models import User
from post.serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions

# Create your views here.

# def post(request):

#     return HttpResponse('POST picture')
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create.html'
    success_url=reverse_lazy('list')

    def form_valid(self,form):
        form.instance.owner = self.request.user
        breakpoint()
        return super().form_valid(form)


class PostList(ListView):
    model = Post 
    template_name = 'post_list.html'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PostDetail(DetailView):
    model = Post
    template_name =  'post_detail.html'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    