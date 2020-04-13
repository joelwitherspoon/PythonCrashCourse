from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """The home page for blogs"""
    return render(request,'blogs/index.html')

def posts(request):
    """Show all posts"""
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts':posts}
    return render(request,'blogs/posts.html',context)

def post(request,blogpost_id):
    """Show a single post"""
    post = BlogPost.objects.get(id=blogpost_id)
    context={'post':post}
    return render(request,'blogs/post.html',context)

def new_post(request):
    """Add a new post"""
    if request.method != 'POST':
        #No data submitted create a blank form
        form = BlogPostForm()
    else:
        #Post submitted, process data
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:posts'))
        
    context = {'form':form}
    return render(request,'blogs/new_post.html',context)

    
