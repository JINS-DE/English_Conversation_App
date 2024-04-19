from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            print("인증성공")
            login(request, user)
        else:
            print("인증실패")
    return render(request,"user/login.html")

def logout_view(request):
    logout(request)
    return redirect("users:login")

def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        level = request.POST['level']

        user = User.objects.create_user(username, email, password )
        user.last_name = lastname
        user.first_name = firstname
        user.level = level
        user.save()
        return redirect("users:login")
    return render(request,"user/signup.html")