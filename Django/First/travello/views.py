from travello.models import Destination
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.

def index(request):
        
        dests = Destination.objects.all()
        return render(request,"index.html",{'dests':dests})

def dest(request):
        return render(request,"destinations.html")
'''        if User.is_authenticated:
                #return render(request,"destinations.html")
                print("LOGGED")
        else:
                print("Not LOGGED")
                #return redirect('login')
   '''     