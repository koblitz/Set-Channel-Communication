# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
# Table Comments
class Comments(models.Model):
  date = models.DateField()
  author = models.CharField(max_length=30)
  text = models.CharField(max_length=70)
