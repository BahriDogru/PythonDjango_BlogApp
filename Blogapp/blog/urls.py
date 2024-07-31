from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blogs', views.blogs, name="blogs"),
    path('blogs/<slug:slug>', views.blog_details, name="blog_details"),
    path('category/<slug:slug>', views.blogs_by_category, name="blogs_by_category"),
    path('addblog', views.addblog, name="addblog"),
    path('profile', views.profile, name="profile"),
    path('settings', views.settings, name="settings"),
    # path('uploads/', views.uploads, name='uploads'),    
]
