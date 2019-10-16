from django.urls import path, include

from . import views

app_name= "accounts"

urlpatterns = [
    path("new/",views.ProfileCreateView.as_view(), name="Profile"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("<int:pk>/profile/", views.ProfileDetailView.as_view(), name="details")
]
