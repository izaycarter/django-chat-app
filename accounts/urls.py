from django.urls import path, include

from . import views

app_name= "accounts"

urlpatterns = [
    path("new/",views.ProfileCreateView.as_view(), name="profile"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("profile/", views.ProfileDetailView.as_view(), name="details"),
    path("update_profile/<int:pk>", views.UpdateProfileView.as_view(), name="update_profile"),
]
