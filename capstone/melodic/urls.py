from django.urls import path
from . import views

urlpatterns = [
    #Splashpage path
    path('', views.Splash.as_view(), name="splash"),
    #path for login
    path('login/', views.Login.as_view(), name="login"),
    #signup
    path('signup/', views.Signup.as_view(), name="signup"),
    #home page, shows posts, allows creation of posts
    path('home/', views.Home.as_view(), name="home"),

]