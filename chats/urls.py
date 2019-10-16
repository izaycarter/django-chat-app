from django.urls import path, include

from . import views

app_name= "chats"



urlpatterns = [
    path("", views.RoomListView.as_view(), name="room_list"),
    path("new/", views.RoomCreateView.as_view(), name="create"),
    path("<int:pk>/", views.RoomDetailView.as_view(), name="detail"),
    path("<int:pk>/request",views.CommentCreateView.as_view() , name="request_comment"),
]
