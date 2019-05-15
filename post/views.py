from django.shortcuts import render,HttpResponse
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy 
from .forms import PostForm
from .models import Post, Like
from django.contrib.auth.models import User
from post.serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions
from itertools import chain

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create.html'
    success_url=reverse_lazy('list')

    def form_valid(self,form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
        
class LikeList(ListView):
    model = Like
    template_name = "post_detail.html"
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
class PostList(ListView):
    model = Post 
    template_name = 'post_list.html'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) 

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        l=[]
        m = list(Like.objects.filter(user=self.request.user).values('post')) 

        for i in m:
            l.append(i.get('post'))

        context['liked_post'] = l
        return context

class LikeCount(ListView):
    model = Like
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



def like(request, pk):
    user = request.user
    post = Post.objects.filter(id=pk).first()
    
    like_obj,created=Like.objects.get_or_create(post=post, user=user)


    if not created:
       like_obj.delete()

    return HttpResponse(PostList.as_view())


def index(request):
    user = request.user
    like_post = Like.objects.filter(user=user).values('post__id')
    return HttpResponse(list(like_post))
    