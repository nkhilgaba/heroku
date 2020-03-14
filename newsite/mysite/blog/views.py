from django.http import HttpResponse,Http404
from django.shortcuts import render, redirect
from blog.models import Post
from django.views.generic.detail import DetailView

def post_detail(request,blog_id):
    try:
    	blog=Post.objects.get(pk=blog_id)

    except blog.DoesNotExist:
    	raise Http404("Blog does not exist")	

    context={'blog':blog}
    
    return render(request=request,template_name='blog/post.html',context=context)