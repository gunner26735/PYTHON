from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout

# Create your views here.

def log(request):
    if request.method == 'POST':
        uname = request.POST['username']
        upass = request.POST['pass']

        user = auth.authenticate(username=uname,password=upass)

        if user != None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid UserName or PAssword")
            return redirect('login')
        #if User.objects.filter(username=uname).exists() and User.objects.filter(username=uname).exists()
    else:
        return render(request,"login.html") 

def reg(request):
    if request.method == 'POST':
        firstn = request.POST['fname']
        lastn = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        pass1 = request.POST['password_1']
        pass2 = request.POST['password_2']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=pass1,email=email,first_name=firstn,last_name=lastn)
                user.save()
                print("User created")           
        else:
            messages.info(request,'Password does not Match')
            return redirect('register')
        return redirect("login")
    
    else:
        return render(request,"register.html")


def lout(request):
    logout(request)
    return redirect("/")