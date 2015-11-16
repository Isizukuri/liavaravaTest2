#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class TextNote(models.Model):
    """Text Notes"""

    text = models.TextField(
        verbose_name=u"Tекстові поля")
