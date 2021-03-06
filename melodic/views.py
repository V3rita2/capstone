from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Track, Comment

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
@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("title")

        if name != None:
            context["tracks"] = Track.objects.filter(title__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["tracks"] = Track.objects.all()
            context["header"] = "Popular Tracks"
        return context

#Track creation view
@method_decorator(login_required, name='dispatch')
class TrackCreate(CreateView):
    model = Track
    fields = ['title', 'cover', 'body', 'author']
    template_name = 'track_create.html'

    #user validation
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TrackCreate, self).form_valid(form)
    
    def get_success_url(self):
        print(self.kwargs)
        return reverse('track_detail', kwargs={'pk': self.object.pk})

    success_url = "/home/"

#track update and delete views
@method_decorator(login_required, name='dispatch')
class TrackUpdate(UpdateView):
    model = Track
    fields = ['title', 'body', 'cover']
    template_name = 'track_update.html'
    success_url = '/home/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TrackUpdate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class TrackDelete(DeleteView):
    model = Track
    template_name = 'track_delete_confirm.html'
    success_url = "/home/"

#track detail view
@method_decorator(login_required, name='dispatch')
class TrackDetail(DetailView):
    model = Track
    template_name = 'track_detail.html'

#comment creation view
@method_decorator(login_required, name='dispatch')
class CommentCreate(View):

    def post(self, request, pk):
        body = request.POST.get("body")
        track = Track.objects.get(pk=pk)
        Comment.objects.create(body=body, track=track)
        return redirect('track_detail', pk=pk)

#profile page
@method_decorator(login_required, name='dispatch')
class Profile(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["tracks"] = Track.objects.filter(author=self.request.user)

        return context