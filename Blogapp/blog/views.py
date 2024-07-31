from django.shortcuts import render
from .models import  Blog, Category
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
def home(request):
    return render(request,'blog/index.html',{
        "blogs": Blog.objects.all(),
        "categories": Category.objects.all()
    })

def blogs(request):
    return render(request,'blog/blogs.html',{
        "blogs": Blog.objects.all(),
        "categories": Category.objects.all()
    })

def profile(request):
    return render(request,'blog/profile.html')

def settings(request):
    return render(request,'blog/settings.html')

def addblog(request):
    if request.method =="POST":
        title = request.POST["title"]
        story = request.POST["story"]
        image = request.FILES["image"]
        categories = request.POST.getlist("categories")
        blog = Blog.objects.create(title=title, story=story, image=image)
        blog.save()
        
        for category_id in categories:
            category = Category.objects.get(id=category_id)
            blog.categories.add(category)

        blog.save()

    return render(request,'blog/addblog.html', {"categories": Category.objects.all()})

def blog_details(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request,"blog/blog_details.html", {
        "blog":blog
    })

# def uploads(request):
#     # Buraya dosya yükleme işlemlerini ekleyin
#     return render(request,'blog/profile.html')

def blogs_by_category(request, slug):
    context={
        "blogs": Blog.objects.filter(categories__slug=slug),
        "categories": Category.objects.all()
    }
    return render(request,'blog/blogs.html',context)