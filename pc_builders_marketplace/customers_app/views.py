from customers_app.forms.sign_up_form import signUpForm
from customers_app.forms.log_in_form import logInForm
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import render, redirect

# Define method for rendering the home page
def home_page(request):
    context = {'form': signUpForm()}
    return render(request, 'customers_app/index.html', context)

# Define a method for the traditional sign up
def sign_up(request):
    if request.method == 'POST':
        # Instantiate the form with POST data
        form = signUpForm(request.POST)

        if form.is_valid():
            # if the form is valid, clean the data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            # Get the user model
            User = get_user_model()

            # This is an inbuilt Django method that creates a user instance in the database
            User.objects.create_user(username=username, email=email, password=password)
            
            # This is a success message that is sent upon succesfull signup
            messages.success(request, "Sign up successful! Please log in")

            return redirect('log_in')
    else:
        # if it is a get request, we can render an empty form
        form = signUpForm()

    # Render the log in page with the form (either empty or with errors)
    return render(request, 'customers_app/sign_up.html', {'form': form})

# Define  method for log in
def log_in(request):
    if request.method == 'POST':
        # Instantiate the form with POST data
        form = logInForm(request.POST)

        if form.is_valid():
            # if the form is valid, clean the data
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Check if the "Remember me" checkbox is checked
            remember_me = form.cleaned_data.get('remember_me')

            # Attempt to authenticate the user with the provided credentials
            user = authenticate(request, email=email, password=password)

            if user is not None:

                # If authentication is successful, log the user in
                login(request, user)

                # Set the rememeber me_value
                if remember_me:
                    request.session.set_expiry(settings.SESSION_COOKIE_AGE)
                else:
                    request.session.session.set_expiry(0)

                # Redirect the user
                return redirect('home_page')
            else:
                # If authentication fails, add a non-field error to the form
                form.add_error(None, "Invalid email or password")

    else:
        # If it is a get requst, we can render an empty form
        form = logInForm()

    # Render the log in page with the form (either empty or with errors)
    return render(request, 'customers_app/log_in.html', {'form': form})

# Define method for rendering the log out page
def logout_page(request):
    logout(request)
    return redirect('home_page')