from django.db import models

class layanan(models.Model):
    platfrom = models.CharField(max_length=50)

    berupa = models.CharField(max_length=50)
