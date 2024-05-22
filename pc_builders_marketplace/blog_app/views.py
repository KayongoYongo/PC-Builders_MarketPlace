from blog_app.forms.blog_form import BlogForm
from blog_app.models import Blog
from customers_app.models import CustomUser
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def blog_list(request):
    """
    This function returns all the blog posts
    """
    blogs = Blog.objects.all()
    return render(request, 'blog_app/blog_list.html', {'blogs': blogs})

def view_blog(request, id):
    """
    This function enables a user to view a single blog post
    """
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog_app/blog_detail.html', {'blog': blog})

# This makes sure that only a user that is logged in can create a blog
@login_required
def create_blog(request):
    """
    This function creates a blog in Django
    """
    if request.method == 'POST':
        # Instantiate the form with POST data
        form = BlogForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            status = form.cleaned_data['status']
            author = request.user

            # Show the output information
            print(title, content, author, status)

            # Create the blog post
            Blog.objects.create(title=title, content=content, status=status, author=author)

            return redirect('blog_list')
    else:
        form = BlogForm()

    return render(request, 'blog_app/add_blog.html', {'form': form})

@login_required
def view_my_blogs(request):
    """
    This function returns blogs created by the individual user
    """
    user = request.user
    blogs = Blog.objects.filter(author=user)
    return render(request, 'blog_app/my_blogs.html', {'blogs': blogs, 'username': user.username})

@login_required
def delete_blog(request, id):
    """
    This function deletes a blog 
    """
    blog = get_object_or_404(Blog, id=id)

    # Delete the blog
    blog.delete()

    # Send the user a message
    messages.success(request, "Blog post deleted successfully.")
    return redirect('view_my_blogs')