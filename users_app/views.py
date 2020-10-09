from django.contrib import messages
from django.shortcuts import render,redirect
from users_app.form import CustomRegisterForm
# Create your views here.
from django.contrib.auth import views


def register(request):
    if request.method == 'POST':
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("User is registrerd successfully!  login to the site"))
            return redirect('register')
    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})

