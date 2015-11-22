from django.contrib import admin

from .models import TextNote, HttpRequestLogEntry

# Register your models here.

admin.site.register(TextNote)
admin.site.register(HttpRequestLogEntry)
