from django.shortcuts import render
from .models import blog

# Create your views here.
def index(request):
    list =  blog.objects.all().order_by('-id')[:10]
    bool=True
    return render(request,'index.html',{'list':list,'bool':bool})

def index1(request):
    list=blog.objects.all().order_by('-id')
    bool=False
    return render(request,'index.html',{'list':list,'bool':bool})

def about(request):
    return render(request,'about.html')

def post(request,i):
    li=blog.objects.get(id=i)
    return render(request,'post.html',{'post':li})   