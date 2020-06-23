from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context ={'title':'NO one','welcome':'欢迎访问自动化测试平台'}
    return render(request,'tpTest/index.html',context)