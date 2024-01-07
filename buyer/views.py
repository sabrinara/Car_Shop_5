from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm ,SetPasswordForm
from .forms import RegisterForm
from cars.models import Car

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            messages.success(request, 'Signup successful. Please login.')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'form.html', {'form': form, 'title': 'Sign Up'})

def user_login(request):
    if request.method == 'POST':
       form = AuthenticationForm(request, data=request.POST)
       if form.is_valid():
           user = form.cleaned_data['username']
           password = form.cleaned_data['password']
           user = authenticate(username=user, password=password)
           if user is not None:
               login(request, user)
               messages.success(request, 'You have successfully logged in.')
               return redirect('buyer')

    else:
        form = AuthenticationForm()

    return render(request, 'form.html', {'form': form , 'title': 'Login'})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')

# @login_required
def buyer(request):
    if request.user.is_authenticated:
        bought_cars = Car.objects.filter(buy=request.user)
        return render(request, 'buyers.html', {'bought_cars': bought_cars})
    else:
        return redirect('login')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid(): 
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'form.html', {'form': form , 'title': 'Change Password'})

def change_password2(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid(): 
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        form = SetPasswordForm(request.user)

    return render(request, 'form.html', {'form': form, 'title': 'Change without old Password'})