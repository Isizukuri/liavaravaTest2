#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class TextNote(models.Model):

    """Text Notes"""

    text = models.TextField(
        verbose_name=u"Tекстові поля")


class HttpRequestLogEntry(models.Model):

    """Requests"""

    date = models.DateTimeField('Request date/time', db_index=True)
    request_method = models.CharField('Method', max_length=6, db_index=True)
    path = models.CharField(max_length=256)

    def __unicode__(self):
        return u'%s [%s] %s' % (
            self.date.strftime('%Y-%m-%d %H:%M:%S'),
            self.request_method,
            self.path
        )
