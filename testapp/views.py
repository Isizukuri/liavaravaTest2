from django.views.generic import ListView
from .models import TextNote


class TextNoteList(ListView):
    model = TextNote
