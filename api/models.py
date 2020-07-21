from django.db import models

# Create your models here.
class Volunteer(models.Model):
    name = models.CharField(max_length=32, blank=False, default='')
    group = models.CharField(max_length=2, blank=False, default='')
    created = models.DateTimeField(auto_now_add=True)