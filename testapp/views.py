import random

from django.views.generic import TemplateView, ListView
from django.http import HttpResponse

from .models import TextNote


class TextNoteList(ListView):
    template_name = "index.html"
    model = TextNote


class WidgetGet(TemplateView):
    template_name = "widget.html"


def widget_return(request):
    note = random.choice(TextNote.objects.all()).text
    response = u"document.write('<div>" + note + u"</div>')"
    return HttpResponse(response)
