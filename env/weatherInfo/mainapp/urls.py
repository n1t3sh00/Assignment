from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.home,name='home')

]
