import random

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse

from .models import TextNote, HttpRequestLogEntry


class TextNoteList(ListView):
    template_name = "index.html"
    model = TextNote


class WidgetGet(TemplateView):
    template_name = "widget.html"


def widget_return(request):
    note = random.choice(TextNote.objects.all()).text
    response = u"document.write('<div>" + note + u"</div>')"
    return HttpResponse(response)


def requests_log(request):
    entries = HttpRequestLogEntry.objects.all()
    object_list = entries[:10].reverse
    return render(request, 'requests.html', {'object_list': object_list})
