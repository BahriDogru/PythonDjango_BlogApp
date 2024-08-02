from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import  Blog
from account.models import UserProfile

# Create your views here.
def login_request(request):
    if request.method=="POST":
        username= request.POST["username"]
        password= request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'account/login.html', {
                "error":"Kullanıcı adı ya da parola yanlış"
            })

    return render(request, 'account/login.html')

def register_request(request):
    if request.method=="POST":
        username= request.POST["username"]
        email= request.POST["email"]
        firstname= request.POST["firstname"]
        lastname= request.POST["lastname"]
        password= request.POST["password"]
        repassword= request.POST["repassword"]
        picture = request.FILES["picture"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request,'account/register.html', {
                    "error":"username kullanılıyor.",
                    "username":username,
                    "firstname":firstname,
                    "lastname":lastname,
                    "email":email,
                 })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request,'account/register.html', {
                        "error":"email kullanılıyor.",
                        "username":username,
                        "firstname":firstname,
                        "lastname":lastname,
                        "email":email,
                    })
                else:
                    user = User.objects.create_user(username=username, email=email, first_name=firstname,last_name=lastname,password=password)
                    user.save()
                    UserProfile.objects.create(user=user, avatar=picture)
                    return redirect("login")

        else:
             return render(request,'account/register.html', {
                "error":"Parolalar eşleşmiyor",
                "username":username,
                "firstname":firstname,
                "lastname":lastname,
                "email":email,
            })

        
    return render(request, 'account/register.html')


def profile(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        context = {
            "user": request.user,
            "image": user_profile
        }
    else:
        context ={}
    return render(request,'account/profile.html', context)


def myblogs(request):
    if User.is_authenticated:
        user = request.user
        user_profile = UserProfile.objects.get(user=request.user)
        context={
               "users":request.user,
               "blogs" : Blog.objects.filter(author__username=user),
               "image":user_profile
            }

    return render(request,'account/myblogs.html', context)

def updateprofile(request):
    if User.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        context={
               "image":user_profile,
               "users":request.user,
            }
    if request.method =="POST":
        email= request.POST["email"]
        firstname= request.POST["firstname"]
        lastname= request.POST["lastname"]
        User.objects.update(email=email, first_name=firstname, last_name=lastname)
        return redirect('profile')
    
    return render(request, 'account/updateprofile.html', context)


def logout_request(request):
    logout(request)
    return redirect('home')