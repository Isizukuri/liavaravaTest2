"""livaravaTest2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from testapp.views import TextNoteList, WidgetGet
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
                       # TestApp urls
                       url(r'^$', TextNoteList.as_view(), name='home'),
                       url(r'^widget/$', WidgetGet.as_view(), name='widget'),
                       url(r'^widget_return/$', 'testapp.views.widget_return',
                           name='widget_return'),
                       url(r'^requests/$', 'testapp.views.requests_log',
                           name='requests'),
                       url(r'^admin/', include(admin.site.urls)),
                       ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
