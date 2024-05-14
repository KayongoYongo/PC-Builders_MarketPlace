from django.shortcuts import render
from customers_app.forms.sign_up_form import signUpForm

# Create your views here.
def sign_up_page(request):
    context = {'form': signUpForm()}
    return render(request, 'pc_builders_marketplace_app/sign_up.html', context)