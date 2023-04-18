from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta

# Create your models here.
class UserExtend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField()
    
    def __str__(self):
       return self.user.username
     
class Book(models.Model): 
    # user = models.ForeignKey(User,default = 1, on_delete=models.CASCADE)
    book_id = models.CharField(max_length=50) 
    book_name = models.CharField(max_length=50) 
    subject = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    
    def __str__(self): 
        return self.book_name +'['+str(self.book_id)+']'
    
class Student(models.Model):
    student_id = models.CharField(max_length=50)
    student_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.student_name +'['+str(self.student_id)+']'
    
def expiry():
    return datetime.today() + timedelta(days=15)

class IssueBook(models.Model):
    book_id = models.CharField(max_length=50) 
    student_id = models.CharField(max_length=50)
    issue_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)
    
    def __str__(self):
        return self.student_name 
    
class ReturnBook(models.Model):
    book_id=models.CharField(max_length=50)
   

    
    
    
