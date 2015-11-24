import random

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.core import serializers

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
    if request.is_ajax():
        pass
    else:
        entries = list(HttpRequestLogEntry.objects.all())
        entries.reverse()
        entries = serializers.serialize("json", entries[:10])
        return render(request, 'requests.html', {'object_list': entries})
