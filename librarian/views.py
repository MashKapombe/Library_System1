from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Book, Student, IssueBook, ReturnBook
# from .forms import LoginForm, SignUpForm

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


    return render(request, 'librarian/login.html')


def signupPage(request):
    if request.method == "POST":
        username = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['pass']
        

        # push to the db
        if User.objects.filter(username=username).exists():
            messages.info(request, 'username taken')
            return redirect('signup')

        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email taken')
            return redirect('signup')

        else:

            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.phone = phone
            # myuser.save()

            messages.success(request, 'Account successfully created')

            return redirect('login')


    return render(request, 'librarian/signup.html')


def dashboard(request):

    # if request.session.has_key('is_logged'):

    books = Book.objects.all()
    
    context = {
        'books': books
    }

    return render(request, 'librarian/dashboard.html', context)


def signout(request):
    logout(request)
    messages.success(request, 'logout successfully')
    return redirect('index')


def addbook(request):
    
    # if request.session.has_key('is_logged'):
    if request.method == 'POST':
        # user_id = request.session["user_id"]
        # user1 = User.objects.get(id=user_id)
        book_id = request.POST["book_id"]
        book_name = request.POST["book_name"]
        subject = request.POST["subject"]
        status = request.POST["status"]

        book = Book.objects.create(
            book_id=book_id, book_name=book_name, subject=subject, status=status)
        book.save()
        
        return redirect('dashboard')

    return render(request, 'librarian/addbook.html')


def addstudent(request):
    if request.method == "POST":
        student_id = request.POST["studentid"]
        student_name = request.POST["studentname"]
        
        student = Student.objects.create(student_id=student_id, student_name=student_name)
        student.save()
        
        return redirect('viewstudent')

    return render(request, 'librarian/addstudent.html')


def viewstudent(request):
    student = Student.objects.all()
    
    return render(request, 'librarian/viewstudent.html', {'student':student})


def issuebook(request):
    return render(request, 'librarian/issuebook')


def returnbook(request):
    return render(request, 'librarian/returnbook.html')
