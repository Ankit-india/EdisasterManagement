from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):

    return render(request, 'index.html')

def VulnerabilityProfile(request):
    return render(request, 'VulnerabilityProfile.html')

def DM_Cycle(request):
    return render(request, 'DM_Cycle.html')

def Earthquake(request):
    return render(request, 'Earthquake.html')

def Tsunami(request):
    return render(request, 'Tsunami.html')

def Flood(request):
    return render(request, 'Flood.html')

def UrbanFloods(request):
    return render(request, 'UrbanFloods.html')

def Landslides(request):
    return render(request, 'Landslides.html')

def Cyclone(request):
    return render(request, 'Cyclone.html')

def HeatWave(request):
    return render(request, 'HeatWave.html')

def Nuclear(request):   
    return render(request, 'Nuclear.html')

def Biological(request):
    return render(request, 'Biological.html')

def Chemical(request):
    return render(request, 'Chemical.html')

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            print('Loged in Successfully')
            return redirect('/')
        else:
            print('Invalid Credentials')
            messages.info(request, 'Invalid Credentials')
            return redirect('/')

    else:
        return redirect('/')

def SignUp(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['email']

        CreatUser = User.objects.create_user(first_name=firstName, last_name=lastName, email=email, password=password,  username=username,)
        CreatUser.save()
        print('User Created Successfully')
        return redirect('/')
    else:
        return redirect('/')

def LogOut(request):
    auth.logout(request)
    return redirect('/')
