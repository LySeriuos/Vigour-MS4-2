from django.shortcuts import render,reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.models import User

from .models import Blogs
from .forms import BlogForm


# Create your views here.

def blogs(request):
    """A view to show individual product details"""
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
            blogs = form.save() 
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
