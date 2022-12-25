
from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
import requests
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import City
from .forms import CityForm
        # Create your views here.
def home (request):
   
     cities = City.objects.all()
     url = 'https://api.openweathermap.org/data/2.5/weather{}&units-imperial&appid=0d34ac1f2677fb744791c29e1cbe5368'
     
     if request.method == 'POST' :
          form = CityForm (request.POST)
          form.save()

     form = CityForm()
     weather_data = []
     for city in cities:
          response = request.POST.get(url.format(city))
          #city_weather = r.json()
          import json
          city_weather = json()
         

          weather = {
               'city':city,
               'temperature':city_weather ['main']['temp'],
               'description': city_weather ['weather'][0]['description'],
               'icon': city_weather ['weather'][0]['icon'],
               'humidity':city_weather ['main']['humidity'],
               'pressure': city_weather['main']['pressure']
             
        }
          weather_data.append(weather)
     context = {'weather_data' : weather_data,'form':form}    
     return render(request,'home.html',context)



def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password1')
        my_user=User.objects.create_user(username= uname,email= email,password=password)
        my_user.save()
        return redirect('login')
        
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render (request,'login.html')

@login_required
def delete(request, name):
    request.user.city.all().filter(name=name).delete()
    return redirect('Hhome.html')