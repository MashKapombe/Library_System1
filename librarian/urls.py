from django.urls import path
from . import views

urlpatterns = [  
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('signup/', views.signupPage, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addbook/', views.addbook, name='addbook'), 
    path('signout/', views.signout, name='signout'),
]