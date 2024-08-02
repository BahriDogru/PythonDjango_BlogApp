from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_request, name="login"),
    path('register', views.register_request, name="register"),
    path('logout', views.logout_request, name="logout"),  
    path('profile', views.profile, name="profile"),
    path('myblogs', views.myblogs, name="myblogs"),
    path('updateprofile', views.updateprofile, name="updateprofile")
]
