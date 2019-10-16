from django import forms
from parsley.decorators import parsleyfy

from .models import Room

class RoomForm(forms.ModelForm):
    name = forms.CharField(min_length=3, required=True)

    class Meta:
        model = Room
        fields =["name"]
