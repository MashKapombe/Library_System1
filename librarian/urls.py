from django.urls import path
from . import views



urlpatterns = [  
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('signup/', views.signupPage, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addbook/', views.addbook, name='addbook'), 
    path('addstudent/', views.addstudent, name='addstudent'), 
    path('viewstudent/', views.viewstudent, name='viewstudent'), 
    path('issuebook/', views.issuebook, name='issuebook'),
    path('viewissuedbook/', views.viewissuedbook, name='viewissuedbook'), 
    path('returnbook/', views.returnbook, name='returnbook'), 
    path('signout/', views.signout, name='signout'),
    path('editbook/<int:id>', views.editbook, name='editbook'), 
    path('<int:id>/updatebook/', views.updatebook, name='updatebook'), 
    path('deletebook/<int:id>',views.deletebook,name='deletebook'),
]