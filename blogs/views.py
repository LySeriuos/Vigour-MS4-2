from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.models import User

from .models import Blogs
from .forms import BlogForm


# Create your views here.

def blogs(request):
    """A view to show all blogs"""
    if request.method == 'GET':
        blogs = Blogs.objects.all()
        context = {
            'blogs': blogs,
        }
    else:
        return redirect('home')
    return render(request, 'blogs/blogs.html', context)


@login_required
def add_blog(request):
    """ Add a blog to the community page """
    if request.method == 'POST':
        def sample_view(request):
            current_user = request.user
            print(current_user.id)
        # capture image if it was submited
        form = BlogForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            form.instance.author = user
            blog = form.save() 
            messages.success(request, 'Successfully added blog!')
            return redirect(reverse('blogs'))
        else:
            messages.error(request, 'Failed to uppload teh blog. Please check the form!')
    else:
        form = BlogForm()
         
    template = 'blogs/add_blog.html'
    context = {
        'form': form,
        }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """ Edit a blog in the store """
    if not request.user.is_superuser:
        messages.error(request, 'You have not permit to manipulate blogs, login as a Admin!')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blogs, pk=blog_id)
    if request.method == 'POST':
        # get the blog information to the form
        form = BlogForm(request.POST, request.FILES, instance=blog)
        # checking if changed information is valid
        if form.is_valid():
            # save the blog form
            form.save()
            # send the message of success or fail
            messages.success(request, 'The blog post is updated!')
            return redirect(reverse('blogs'))
        else:
            messages.error(request, 'Failed to update the blog post. Check the form!')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.title}')
    template = 'blogs/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """ Delete a blog from the store """
    if not request.user.is_superuser:
        messages.error(request, 'You have not permit to manipulate blogs, login as a Admin!')
        return redirect(reverse('home'))        
    blog1 = get_object_or_404(Blogs, pk=blog_id)
    blog1.delete()
    messages.success(request, 'The blog is deleted!')
    return redirect(reverse('blogs'))
