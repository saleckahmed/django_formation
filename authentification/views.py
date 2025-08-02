from django.shortcuts import render, redirect
from django.http import response
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get('next', '/annonce/')
            return redirect(next_url)
        else:
            return render(request, 'login.html', {
                'form': LoginForm(),
                'message': 'Check your information'
            })
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/auth/login/') 
        else:
            return render(request, 'register.html', {'form': form}) 

    elif request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form':form})
