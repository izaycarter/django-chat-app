from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse ,reverse_lazy

from .models import Room, Comment
from .forms import RoomForm

class RoomListView(generic.ListView):
        model = Room
        template_name = "chats/room_list.html"


class RoomCreateView(generic.CreateView):
    form_class = RoomForm
    template_name = "chats/room_create.html"


class RoomDetailView(generic.DetailView):
    model = Room
    template_name = "chats/room_detail.html"


    def request_comment(request, pk):
        comment = Comment()
        comment.text = request.POST['text']
        comment.room_id = pk
        comment.save()

        return HttpResponseRedirect(reverse('chats:detail', args=(pk,)))
