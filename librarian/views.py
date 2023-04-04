from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Book, Student, IssueBook, ReturnBook
from datetime import datetime,timedelta,date
# from django.db.models import Q


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

@login_required(login_url='login')
def dashboard(request):
    book = Book.objects.all()
    
    if 'q' in request.GET:
        q = request.GET['q']
        book = Book.objects.filter(book_name__icontains=q)
       
    context = {'book':book}
    return render(request, 'librarian/dashboard.html', context)


def signout(request):    
    logout(request)
    messages.success(request, 'logout successfully')
    return redirect('index')

@login_required(login_url='login')
def addbook(request):  
    # if request.session.has_key('is_logged'):
    if request.method == 'POST':
        book_id = request.POST["book_id"]
        book_name = request.POST["book_name"]
        subject = request.POST["subject"]
        status = request.POST["status"]

        book = Book.objects.create(
            book_id=book_id, book_name=book_name, subject=subject, status=status)
        book.save()
        
        return redirect('dashboard')

    return render(request, 'librarian/addbook.html')

@login_required(login_url='login')
def addstudent(request):
    if request.method == "POST":
        student_id = request.POST["studentid"]
        student_name = request.POST["studentname"]
        
        student = Student.objects.create(student_id=student_id, student_name=student_name)
        student.save()
        
        return redirect('viewstudent')

    return render(request, 'librarian/addstudent.html')

@login_required(login_url='login')
def viewstudent(request):
    student = Student.objects.all()
    
    return render(request, 'librarian/viewstudent.html', {'student':student})

@login_required(login_url='login')
def issuebook(request): 
    
    issue = IssueBook.objects.all()
    
    if request.method == 'POST': 
            student_id = request.POST.get("student_id")
            book_id = request.POST.get("book_id")
            store = Book.objects.filter(book_id=book_id)
            
            
            def get_category(book):
                
                if book.category == "Not-Issued":
                    
                # book.category == "Issued"
                    obj = IssueBook(student_id=student_id, book_id=book_id)
                    obj.save()
                    book.save() 
                    
                    
            category_list = list(set(map(get_category, store))) 
              
                   
    else:
                     
        messages.error(request," Book already issued !!!")
       
      
        # category_list = list(set(map(get_category, store)))
        
        # Issue=IssueBook.objects.all()
                  
        # category_list.save()
                                 
        #   return redirect('viewissuedbook')                    
                          
    return render(request,'librarian/issuebook.html', {'issue':issue})
          
@login_required(login_url='login')
def viewissuedbook(request):
        
    issuedbooks = IssueBook.objects.all()
    
    li=[]
    
    for iss in issuedbooks:
          
        issue_date = str(iss.issue_date.day)+'-'+str(iss.issue_date.month)+'-'+str(iss.issue_date.year)
        expiry_date = str(iss.expiry_date.day)+'-'+str(iss.expiry_date.month)+'-'+str(iss.expiry_date.year)
                
        days = (date.today()-iss.issue_date)
        d = days.days
        fine = 0
        
        if d > 15:
            
            day = d-15
            fine = day*10
            
                
        books = list(Book.objects.filter(book_id=iss.book_id))
        students = list(Student.objects.filter(student_id=iss.student_id))
        # print(books)
        # print(students)
            
        i=0
                
        for l in books: 
            
            
            t=(students[i].student_name, students[i].student_id, books[i].book_name, books[i].subject, issue_date, expiry_date, fine)
                    
            i=i+1
                    
            li.append(t)

    return render(request, 'librarian/viewissuedbook.html', {'li':li})

@login_required(login_url='login')
def returnbook(request):
    return render(request, 'librarian/returnbook.html')

@login_required(login_url='login')
def editbook(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'librarian/editbook.html', {'book':book}) 

@login_required(login_url='login')
def updatebook(request, id):
    if request.method == "POST":   
       add = Book.objects.get(id=id)
       add.book_id = request.POST["book_id"]
       add.book_name = request.POST["book_name"]
       add.subject = request.POST["subject"]
       add.status = request.POST["status"]
       add.save()
       return redirect('dashboard')
   
@login_required(login_url='login')   
def deletebook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('dashboard')

    
   

    
        
