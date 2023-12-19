from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import pyttsx3 as ts
import pywhatkit as pwt

# Create your views here.

def register(request) :

    if request.method == 'POST':

        user = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1 :
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=user).exists() :
                messages.info(request, 'Username already exists')
                return redirect('register')
            else :
                user = User.objects.create_user(username = user, email=email, password=password1)
                user.save()
                pob = ts.init()
                pob.say(f"Congratulations {user} You are successfully Rgistered")
                pob.runAndWait()
                return redirect('login')
            
        else :
            messages.info(request, 'Password is not same')
            return redirect('register')
    
    return render(request, "register.html")



def login(request) :
    if request.method == 'POST' :
        user = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(username = user, password=password)

        if user is not None :
            auth.login(request,user)
            pyobj = ts.init()
            pyobj.setProperty("rate",180) 
            pyobj.say(f"Congratulations {user} You are successfully loged into your account")
            pyobj.runAndWait()
            return render(request, 'user_login.html')
        else :
            messages.info('Credentials Invalid')
            return redirect('login')
        return render(request, 'login.html')
    else :
        # pyobj = ts.init()
        # pyobj.setProperty("rate",120) 
        # pyobj.say("Congratulations You are successfully loged into your account")
        # pyobj.runAndWait()
        return render(request, 'login.html')
    

def logout(request) :
    auth.logout(request)
    return redirect('/')