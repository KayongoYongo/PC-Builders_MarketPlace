from customers_app.forms.sign_up_form import signUpForm
from customers_app.forms.log_in_form import logInForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Define method for rendering the home page
def home_page(request):
    context = {'form': signUpForm()}
    return render(request, 'customers_app/index.html', context)

# Define method for rendering sign up page
def sign_up_page(request):
    context = {'form': signUpForm()}
    return render(request, 'customers_app/sign_up.html', context)

# Define method for rendering log in page
def log_in_page(request):
    context = {'form': logInForm()}
    return render(request, 'customers_app/log_in.html', context)

# Define method for rendering log out page
def logout_page(request):
    logout(request)
    return redirect('home_page')