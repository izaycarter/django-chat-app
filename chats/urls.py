from django.urls import path, include

from . import views

app_name= "chats"



urlpatterns = [
    path("", views.StartTemplateView.as_view(), name="start"),
    path("rooms/", views.RoomListView.as_view(), name="room_list"),
    path("new/", views.RoomCreateView.as_view(), name="create"),
    path("<int:pk>/", views.RoomDetailView.as_view(), name="detail"),
    path("<int:pk>/delete_comment", views.CommentDeleteView.as_view(), name="delete_comment"),
    path("<int:pk>/request",views.CommentCreateView.as_view() , name="request_comment"),
    path("<int:pk>/update", views.add_member, name="add_member"),
    path("my-room-list/", views.MyRoomsListView.as_view(), name="my_room_list"),
]
