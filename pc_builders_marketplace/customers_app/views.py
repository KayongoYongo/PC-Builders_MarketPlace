from customers_app.forms.sign_up_form import signUpForm
from customers_app.forms.log_in_form import logInForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Define method for rendering the home page
def home_page(request):
    context = {'form': signUpForm()}
    return render(request, 'customers_app/index.html', context)

# Define method for rendering log in page
def log_in_page(request):
    context = {'form': logInForm()}
    return render(request, 'customers_app/log_in.html', context)

# Define a method for the traditional sign up
def sign_up(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            # This is an inbuilt Django method that creates a user instance in the database
            User.objects.create_user(username=username, email=email, password=password)
            
            # This is a success message that is sent upon succesfull signup
            messages.success(request, "Sign up successful! Please log in")

            return redirect('log_in_page')
    else:
        # if it is a get request, we can render an empty form
        form = signUpForm()
    
    return render(request, 'customers_app/sign_up.html', {'form': form})

# Define method for rendering log out page
def logout_page(request):
    logout(request)
    return redirect('home_page')