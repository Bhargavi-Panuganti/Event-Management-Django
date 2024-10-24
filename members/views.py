from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import RegisterUserForm
from django.http import HttpResponse,HttpRequest


def login_user(request):
    if request.method=='POST':
        username = request.POST["UserName"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('check')
        
        elif user is None:
            messages.success(request,("There was an error with your login..Try Again.."))
            return redirect('user-login')
    else:
        return render(request,'mem/login.html',{})

def Register(request):
    
    if request.method=='POST':
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,('Registration Successful !!'))
            return redirect('cal')
    else:
        form=RegisterUserForm()
    return render(request,'mem/register.html',{'form':form})

def logout_user(request):
    logout(request)
    messages.success(request,("You were Logged out.."))
    return redirect('cal')
