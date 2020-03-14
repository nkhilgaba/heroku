
from django.views.generic import ListView,DetailView
from blog.models import Post
from django.urls import path, re_path, include
# blog.views import BlogDetailView
from . import views

urlpatterns = [

re_path(r'^$',ListView.as_view(queryset=Post.objects.all().order_by('-date')[:25],template_name='blog/blog.html')),

re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post,template_name="blog/post.html")),
#re_path(r'^(?P<pk>\d+)$',BlogDetailView.as_view(),name='blog-detail'),
#path('<int:pk>/', views.post_detail, name='post_detail'),
#path('<int:blog_id>',views.post_detail,name='post_detail'),

]
#	path('<single_slug>',views.single_slug,name='single_slug'),