from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(f'User created {username} {password}')
            return redirect('/')
    else:
        form = UserCreationForm(request.POST)
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(f'User logged in {username} {password}')
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
