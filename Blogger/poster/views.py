from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index3.html', {'posts':posts})

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts':posts})

def register(request):
    if request.method == 'POST':
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       password2 = request.POST['password2']

       if password == password2:
          if User.objects.filter(email=email).exists():
             messages.info(request, 'Email already exist!')
             return redirect('register')
          elif User.objects.filter(username=username).exists():
             messages.info(request, 'Username already exist!')
             return redirect('register')
          else:
              user = User.objects.create_user(email=email, username=username, password=password)
              user.save()
              return redirect('login')
       else:
           messages.info(request, 'Password does not correspond!')
    else:
       return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
          auth.login(request, user)
          return redirect('home')
        else:
            messages.info(request, 'Invalid credentials!!!')
            return redirect('login')
    else:
      return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
    
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

