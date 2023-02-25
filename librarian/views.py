from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'librarian/index.html')
 
def loginPage(request):
    if request.method == "POST":  
    
        username = request.POST.get('username')
        password = request.POST.get('password')
           
        user = authenticate(username=username, password=password)
           
        if user is not None:
            
            login(request, user)
               
            return redirect('dashboard')   
         
        else:
                        
            messages.error(request, 'Bad credentials')

            return redirect('index')
                     
    return render(request, 'librarian/login.html')

def signupPage(request): 
    if request.method == "POST":
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['pass']
        
        # if not uname.isalnum():
        #     messages.error(request, 'username must be alphanumeric')
            
        #     return redirect('index')
        
        myuser = User.objects.create_user(uname, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.phone = phone
        
        # myuser.save()
        
        messages.success(request, 'Account successfully created')
            
        return redirect('login')
              
    return render(request, 'librarian/signup.html')

def dashboard(request):
    
    return render(request, 'librarian/dashboard.html')

def signout(request):
    logout(request)
    messages.success(request, 'logout successfully')
    return redirect('index')

def addbook(request):
    
    return render(request, 'librarian/addbook.html')