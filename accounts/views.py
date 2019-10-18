from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse ,reverse_lazy
from django.views import generic
from django.contrib.auth import login
from django.shortcuts import get_object_or_404

from .models import Profile
from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ProfileCreateView(LoginRequiredMixin, generic.CreateView):
    model = Profile
    template_name = "profile_create.html"
    success_url = reverse_lazy("chats:room_list")
    fields = ("bio","location","avatar",)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    fields = ["bio", "location","avatar",]
    template_name = 'profile_update_form.html'

    success_url = reverse_lazy("accounts:details")


class ProfileDetailView(LoginRequiredMixin,generic.DetailView):
    model = Profile
    template_name = "profile_detail.html"

    def get_object(self):
        # grabs the the pk of the user that is logged in
        return get_object_or_404(Profile, user=self.request.user)
