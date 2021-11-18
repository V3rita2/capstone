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
    #create path for tracks
    path('home/new-track', views.TrackCreate.as_view(), name='track_create'),
    #detail view for tracks
    path('track/<int:pk>/', views.TrackDetail.as_view(), name='track_detail'),
    #create comments
    path('track/<int:pk>/comments/new', views.CommentCreate.as_view(), name='comment_create'),
    #profile page 
    path('profile/', views.Profile.as_view(), name="profile")
]