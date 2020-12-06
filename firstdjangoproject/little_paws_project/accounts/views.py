from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Organistaion_contact
from django.contrib import messages
# Create your views here.



# User registeration
def signup_view(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists() :
                messages.info(request,"Username exists..")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email exists..")
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Incorrect Password..")
            return redirect('signup')

    else:
        return render(request,"signuppage.html")


# User login
def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentails..")
            return redirect("login")
    else:
        return render(request,"loginpage.html")


# logout view
def logout_view(request):
    auth.logout(request)
    return redirect('/')

# render contact page
def contact_view(request):
    if request.method=="POST":
        organisation_name=request.POST['organisation_name']
        email=request.POST['email']
        contact=request.POST['contact']
        message=request.POST['message']
        organisation_details=Organistaion_contact(Organisation_name=organisation_name,Organisation_email=email,Organisation_phone_number=contact,Organisation_message=message)
        organisation_details.save()
        return redirect("/")
    else:
        return render(request,"Contact.html")