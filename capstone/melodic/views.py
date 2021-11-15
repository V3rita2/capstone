from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
from django.urls import reverse

from .models import Track

# Create your views here.

#splashpage 
class Splash(TemplateView):
    template_name = "splash.html"

#login
class Login(TemplateView):
    template_name = "login.html"

#signup
class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

#home (track list)
class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")

        if name != None:
            context["tracks"] = Track.objects.filter(name_icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["tracks"] = Track.objects.all()
            context["header"] = "Popular Tracks"
        return context

