from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse ,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Room, Comment
from .forms import RoomForm


class StartTemplateView(generic.TemplateView):
    template_name = "chats/start.html"


class RoomListView(generic.ListView):
        model = Room
        template_name = "chats/room_list.html"


class RoomCreateView(generic.CreateView):
    form_class = RoomForm
    template_name = "chats/room_create.html"


class RoomDetailView(generic.DetailView):
    model = Room
    template_name = "chats/room_detail.html"


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    fields = ('text',)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.room_id = self.kwargs['pk']
        return super().form_valid(form)


class CommentDeleteView(generic.DeleteView):
    model = Comment

    def get_object(self, queryset=None):
        comment = super(CommentDeleteView, self).get_object()
        if not comment.owner == self.request.user:
            raise Http404
        return comment
    success_url = reverse_lazy("chats:room_list")

def add_member(request, pk):
    # import pdb; pdb.set_trace()
    room = get_object_or_404(Room, pk=pk)
    room.member.add(request.user)

    return HttpResponseRedirect(reverse_lazy("chats:room_list"))


class MyRoomsListView(generic.ListView):
    model = Room
    template_name = "chats/my_rooms.html"

    def get_queryset(self):
        return Room.objects.filter(member=self.request.user)
