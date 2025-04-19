from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from django .contrib import messages

# Create your views here.
def home(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']    

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'You are logged in!')
            return redirect('home')  
        else:
            messages.error(request,'Invalid credentials')
            return redirect('home') 
    else:
        return render(request,'home.html',{})

#def login_view(request):
#    pass

def logout_view(request):
    logout(request)
    messages.success(request,'User logged out!')
    return redirect('home')