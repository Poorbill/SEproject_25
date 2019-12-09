# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name

class my_User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

class minsheng(models.Model):
    street = models.CharField(max_length=64)
    community = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    phone_num = models.CharField(max_length=64)
    detail = models.CharField(max_length=128)
    status = models.CharField(max_length=64)
