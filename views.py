from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
def home(request) : 
    blogs = Blog.objects.all()
    num = Blog.objects.count
    return render(request,'home.html',{'blogs':blogs}) 

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs':blogs})

def detail(request,id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request,'detail.html',{'blog':blog})
    #http 상태 코드 : 서버에 존재하지 않는 코드, 말도안되는 코드를 할 때 404 에러

def new(request):
    return render(request,'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('detail',new_blog.id)
    #redirect 다시 돌아간다는 뜻 원래 페이지로

def edit(request,id):
    edit_blog = Blog.objects.get(id = id)
    return render(request,'edit.html',{'blog':edit_blog})


def update(request,id):
    update_blog = Blog.objects.get(id = id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save()
    return redirect('detail',update_blog.id)

def delete(request,id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')
