from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user1=auth.authenticate(username=username,password=password)

        if user1 is not None:
            auth.login(request,user1)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['confirm password']
        if password==conpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,email=email)
                user.save();
                return redirect('login')

        else:
            messages.info(request,'password is not matching')
            return redirect('register')
        return redirect('/')



    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')