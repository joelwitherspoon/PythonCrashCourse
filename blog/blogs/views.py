from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """The home page for blogs"""
    return render(request,'blogs/index.html')

#Chapter 19 -3 secure Blog posting
@login_required
def posts(request):
    """Show all posts"""
    posts = BlogPost.objects.filter(owner=request.user).order_by('date_added')
    context = {'posts':posts}
    return render(request,'blogs/posts.html',context)

#Chapter 19 -3 secure Blog posting
@login_required
def post(request,blogpost_id):
    """Show a single post"""
    post = BlogPost.objects.get(id=blogpost_id)
    #Only allow blog owner to see post
    check_blog_owner(post.owner,request.user)
    context={'post':post}
    return render(request,'blogs/post.html',context)

#Chapter 19 -3 secure Blog posting
@login_required
def new_post(request):
    """Add a new post"""
    
    if request.method != 'POST':
        #No data submitted create a blank form
        form = BlogPostForm()
    else:
        #Post submitted, process data
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user 
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:posts'))
        
    context = {'form':form}
    return render(request,'blogs/new_post.html',context)

#Chapter 19 -3 secure Blog posting
@login_required
def edit_post(request,blogpost_id):
    """Edit a post"""
    post = BlogPost.objects.get(id=blogpost_id)
    title = post.title
    text = post.text
    check_blog_owner(post.owner,request.user)

    if request.method != 'POST':
        "Initial request; pre-fill form with the current entry"
        form = BlogPostForm(instance=post)
    else:
        """POST data submitted; process data"""
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid() and (post.owner == request.user):
            form.title = title
            form.text = text
            form.save()
           
            return HttpResponseRedirect(reverse('blogs:post', args=[post.id]))
    
    context = {'post':post,
               'title':title,
               'text':text,
               'form':form }
    return render(request, 'blogs/edit_post.html', context)
    
def check_blog_owner(owner, user):
    """Check is the current logged in user is the topic owner"""
    
    if owner != user:
        raise Http404
    else:
        pass         
