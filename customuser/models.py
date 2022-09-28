from django.db import models

class CustomModel(models.Model):

    address = models.TextField('', max_length=500, blank=True)
    bio = models.TextField('', max_length=500, blank=True)
