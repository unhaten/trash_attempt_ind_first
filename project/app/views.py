from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from app.models import Feature


# Create your views here.


def index(request):
    context = {}
    features = Feature.objects.all()
    context['features'] = features
    return render(request, 'index.html', context)


def counter(request):
    words = request.POST['words']
    amount = len(words.split())
    return render(request, 'counter.html', {'amount': amount})


def register(request):
    context = {}

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already used')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, 'register.html')
