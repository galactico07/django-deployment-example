from django.shortcuts import render
from app_five.models import Userprofileinfo
from django.contrib.auth.models import User
from app_five.forms import user_form,Userprofileinfoform
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'app_five/index.html')


def registrations2(request):
    registered = False
    if request.method == 'POST':

        userform = user_form(request.POST)
        profileform = Userprofileinfoform(request.POST)

        if userform.is_valid() and profileform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()

            profile = profileform.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(userform.errors,profileform.errors)
    else:
        userform = user_form()
        profileform = Userprofileinfoform()
    return render(request,'app_five/registrations2.html',context={
    'userform':userform,
    'profileform':profileform,
    'registered':registered,
    })


def registrations(request):
    regi={}
    if request.method == 'POST':

        print(request.POST.get('fname'))
        print(request.POST.get('lname'))
        print(request.POST.get('email'))
        print(request.POST.get('number'))

        user1 = Userprofileinfo.objects.all()
        user2 = User.objects.all()
        print(user2,user1)


    return render(request,'app_five/registrations.html',context=regi)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_five:home'))

@login_required
def special(request):
    return HttpResponse("You are Logged in!!!")

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username,password)

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('app_five:home'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Some tried to login at {}".format(datetime.now()))
            return  HttpResponse("Invalid Login Credentials Provided")
    else:
        return render(request,'app_five/login.html')
