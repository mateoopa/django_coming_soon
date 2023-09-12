from django.db import models
from django.contrib.auth.models import User
from django import forms
import datetime


class Section(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime_added = models.DateTimeField(default=datetime.datetime.now())
    available = models.BooleanField(blank=True, null=True, default=True)
    name = models.CharField(blank=False, null=False, max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'
        db_table = "section"

    def __str__(self):
        return str(self.id)


class Content(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime_added = models.DateTimeField(default=datetime.datetime.now())
    available = models.BooleanField(blank=True, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    tittle = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'content'
        verbose_name_plural = 'contents'
        db_table = "content"

    def __str__(self):
        return str(self.id)
