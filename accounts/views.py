from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse ,reverse_lazy
from django.views import generic
from django.contrib.auth import login

from .models import Profile
from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ProfileCreateView(generic.CreateView):
    model = Profile
    template_name = "profile_create.html"
    success_url = reverse_lazy("chats:room_list")
    fields = ("bio","location","avatar",)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = "profile_detail.html"
    
