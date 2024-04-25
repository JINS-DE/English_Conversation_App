from django.shortcuts import render,redirect

def index_view(request):
    return render(request, 'index.html')  # 로그인한 사용자에게 보여줄 페이지


