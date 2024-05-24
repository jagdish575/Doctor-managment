from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def user_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = make_password(request.POST['password'])
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        qualification = request.POST.get('qualification')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        experience = request.POST.get('experience')
        image = request.FILES.get('image')
        if User.objects.filter(email=email).exists():
            return HttpResponse("Already Exist")
        else:
            user = User.objects.create(
                name=name,
                email=email,
                password=password,
                phone_number=phone_number,
                address=address,
                qualification=qualification,
                gender=gender,
                dob=dob,
                experience=experience,
                image=image
            )
            return redirect('home')  # Use the named URL pattern here

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_password = request.POST.get('password')
        if User.objects.filter(email=email).exists():
            obj = User.objects.get(email=email)
            password = obj.password
            if check_password(user_password, password):
                return redirect('home')  
            else:
                messages.error(request, "Password incorrect")
                return redirect('login') 
        else:
            messages.error(request, "Email not registered")
            return redirect('login')  


def doctor(request):
    doctors = User.objects.all()
    print(doctor)
    return render(request, 'index.html', {'doc' : doctors})
