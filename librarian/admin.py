# Register your models here.
from django.contrib import admin
from .models import Book,IssueBook,ReturnBook,Student
from django.contrib.sessions.models import Session
admin.site.register(Session)

from .models import UserExtend
admin.site.register(UserExtend)

class BookAdmin(admin.ModelAdmin):
    list_display=("book_id","book_name","subject","status")
admin.site.register(Book,BookAdmin)
class IssueBookAdmin(admin.ModelAdmin):
    list_display=("book_id","student_id")
admin.site.register(IssueBook,IssueBookAdmin)
class StudentAdmin(admin.ModelAdmin):
    list_display=("student_name","student_id")
admin.site.register(Student,StudentAdmin)
