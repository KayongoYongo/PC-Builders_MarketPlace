from blog_app.forms.blog_form import BlogForm
from blog_app.models import Blog
from customers_app.models import CustomUser
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import random

# Create your views here.
def blog_list(request):
    """
    Description:
        This function returns all the blog posts available in the database.

    Args:
        request: The HTTP request object that contains metadata about the request.

    Return:
        Renders a template with the blog data
    """

    # Retrieve all blog objects from the database and order them by creation date
    blogs = Blog.objects.all().order_by('-created_at')

    # Featured blog
    featured_blog = random.choice(blogs)

    # Number of blogs per page
    paginator = Paginator(blogs, 2)

    # Get the page number from the request
    page_number = request.GET.get('page')

    # Get the blogs for the current page
    page_obj = paginator.get_page(page_number)

    # Render the blog_list template with the blog data
    return render(request, 'blog_app/blog_list.html', {'page_obj': page_obj, 'featured_blog': featured_blog} )

def view_blog(request, id):
    """
    Description:
        This function enables a user to view a single blog post.

    Args:
        request: The HTTP request object that contains metadata about the request.

    Return:
        Renders a template with the blog data
    """

    # Retrieve the blog object with the given ID, or return a 404 error if not found
    blog = get_object_or_404(Blog, id=id)

    # Render the blog_detail template with the blog data
    return render(request, 'blog_app/blog_detail.html', {'blog': blog})

# This makes sure that only a user that is logged in can create a blog
@login_required
def create_blog(request):
    """
    Description:
        This function enables a user to create a single blog post.
        On GET, the function enables a user to render the add_blog template.

    Args:
        request: The HTTP request object that contains metadata about the request.

    Return:
        On POST request, the function adds a blog post and redirects to the page
        where a user created their individual blog post.
        On GET request, the function renders the add_blog template.
    """

    if request.method == 'POST':
        # Instantiate the form with POST data
        form = BlogForm(request.POST)

        # Validate the form data
        if form.is_valid():
            # Retrieve cleaned data from the form
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            status = form.cleaned_data['status']
            author = request.user

            # Create the blog post
            Blog.objects.create(title=title, content=content, status=status, author=author)

            # Redirect the user to the page showing their blogs
            return redirect('view_my_blogs')
    else:
        form = BlogForm()

    # Render the add blog template with the form data
    return render(request, 'blog_app/add_blog.html', {'form': form})

@login_required
def view_my_blogs(request):
    """
    Description:
        This function returns blogs created by the individual user.

    Args:
        request: The HTTP request object that contains metadata about the request.

    Return:
        The function renders the my_blog template
    """

    # Retrieve the user metadata from the request object
    user = request.user

    # Filter the blogs based on the author
    blogs = Blog.objects.filter(author=user)

    # Render the my_blogs template with the blogs and the username
    return render(request, 'blog_app/my_blogs.html', {'blogs': blogs, 'username': user.username})

@login_required
def delete_blog(request, id):
    """
    This function deletes a blog 
    """
    # Retrieve the blog object with the given ID, or return a 404 error if not found
    blog = get_object_or_404(Blog, id=id)

    # Delete the blog
    blog.delete()

    # Send the user a message
    messages.success(request, "Blog post deleted successfully.")

    # Redirect the user to the page showing their blogs
    return redirect('view_my_blogs')

@login_required
def update_blog(request, id):
    """
    This function handles updating an existing blog post.
    It ensures that the user is logged in and then processes the update form.
    """

    # Retrieve the blog object with the given ID, or return a 404 error if not found
    blog = get_object_or_404(Blog, id=id)

    # Check if the request method is POST, indicating that the form has been submitted
    if request.method == 'POST':
        # Instantiate the form with the data submitted in the request
        form = BlogForm(request.POST)

        # Validate the form data
        if form.is_valid():
            # Retrieve cleaned data from the form
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            status = form.cleaned_data['status']

            # Update the blog object with the new data
            blog.title = title
            blog.content = content
            blog.status = status

            # Save the updated blog object to the database
            blog.save()

            # Display a success message to the user
            messages.success(request, "Blog post updated successfully")

            # Redirect the user to the page showing their blogs
            return redirect('view_my_blogs')
        
    else:
        # If the request method is not POST, instantiate the form with the current blog instance
        form = BlogForm(instance=blog)

    # Render the edit blog template with the form and blog data
    return render(request, 'blog_app/edit_blog.html', {'form': form, 'blog': blog})