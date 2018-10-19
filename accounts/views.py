from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from accounts.forms import RegisterForm
from accounts.models import ChatUser

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            print(user)
            ChatUser.objects.create(user=user)
            login(request, user)
            return redirect('thanks')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def logout(request):
    logout(request)
    return redirect('/')
