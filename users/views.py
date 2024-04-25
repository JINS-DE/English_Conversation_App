from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from .users_form import UserCreateForm,UserModifyForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserModifyForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')  # 수정 완료 후 리다이렉트할 페이지
    else:
        form = UserModifyForm(instance=request.user)
    return render(request, 'user/profile.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')  # 이미 로그인되어 있으면 index 페이지로 리다이렉트

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 로그인 성공 후 index 페이지로 리다이렉트
        else:
            return render(request, 'user/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'user/login.html')

def logout_view(request):
    logout(request)
    return redirect("users:login")

def signup_view(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 회원 가입 즉시 로그인
            return redirect('index')  # 홈페이지 or 대시보드로 리다이렉트
    else:
        form = UserCreateForm()
    return render(request, 'user/signup.html', {'form': form})
