from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=50, unique=True)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    evolution_type = models.CharField(max_length=20)
    evolutions = models.JSONField()
    stats = models.JSONField()