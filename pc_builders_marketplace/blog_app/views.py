from blog_app.forms.blog_form import BlogForm
from blog_app.models import Blog
from django.shortcuts import render, redirect
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
