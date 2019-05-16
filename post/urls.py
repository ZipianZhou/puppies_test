from django.urls import path,re_path,include 
from . import views

urlpatterns = [
    re_path (r'^list/', views.PostList.as_view(),name = 'list'),
    re_path (r'^post/$', views.AddPost.as_view(),name ='add'),
    path ('post/<int:pk>', views.PostDetail.as_view(),name = 'detail'),
    path ('post/like/<int:pk>', views.like, name='like'),
    path ('index/', views.index),