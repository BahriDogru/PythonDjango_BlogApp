from django.shortcuts import render
from .models import  Blog, Category
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from account.models import UserProfile
from datetime import date



# Create your views here.
def home(request):
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            user_profile = UserProfile.objects.create(user=request.user)
        return render(request,'blog/index.html',{
            "blogs": Blog.objects.filter(published_date=date.today()),
            "categories": Category.objects.all(),
            "image": user_profile
        })

    return render(request,'blog/index.html',{
        "blogs": Blog.objects.filter(published_date=date.today()),
        "categories": Category.objects.all()
    })

def blogs(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        return render(request,'blog/blogs.html',{
            "blogs": Blog.objects.all(),
            "categories": Category.objects.all(),
            "image": user_profile
        })
    return render(request,'blog/blogs.html',{
        "blogs": Blog.objects.all(),
        "categories": Category.objects.all()
    })

def addblog(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        if request.method =="POST":
            title = request.POST["title"]
            story = request.POST["story"]
            image = request.FILES["image"]
            categories = request.POST.getlist("categories")
            author = request.user
            blog = Blog.objects.create(title=title, story=story, image=image, author=author)
            blog.save()
            
            for category_id in categories:
                category = Category.objects.get(id=category_id)
                blog.categories.add(category)

            blog.save()
            return redirect("home")
            

        return render(request,'blog/addblog.html', {
            "categories": Category.objects.all(),
            "image": user_profile
            })
    return redirect('login')

def blog_details(request, slug):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        blog = get_object_or_404(Blog, slug=slug)
        return render(request,"blog/blog_details.html", {
            "blog":blog,
            "image": user_profile
        })
    blog = get_object_or_404(Blog, slug=slug)
    return render(request,"blog/blog_details.html", {
        "blog":blog
    })

def blogs_by_category(request, slug):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        context={
            "blogs": Blog.objects.filter(categories__slug=slug),
            "categories": Category.objects.all(),
            "selected_category" : slug,
            "image": user_profile
        }
        return render(request,'blog/blogs.html',context)
    context={
            "blogs": Blog.objects.filter(categories__slug=slug),
            "categories": Category.objects.all(),
            "selected_category" : slug
        }
    return render(request,'blog/blogs.html',context)
    