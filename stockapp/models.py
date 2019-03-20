from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class APISettings(models.Model):

    api_name = models.CharField(max_length=200)
    api_key = models.CharField(max_length=200)
    api_username = models.CharField(max_length=200)
    api_password = models.CharField(max_length=200)
    api_endpoint = models.CharField(max_length=200)
    date_created = models.DateField('Date', auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s User' % self.created_by

    def __unicode__(self):
        return '%s' % self.date_created

    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'

