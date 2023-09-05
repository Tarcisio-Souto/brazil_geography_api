from django.db import models
import uuid

class States(models.Model):

    REGION_CHOICES = [('norte','Norte'),
                      ('nordeste', 'Nordeste'),
                      ('centro_oeste', 'Centro-Oeste'),
                      ('sudeste', 'Sudeste'),
                      ('sul', 'Sul')]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    name = models.CharField(max_length=100, null=False, blank=False)
    population = models.IntegerField(null=False, blank=False)
    region = models.CharField(choices=REGION_CHOICES, null=False, blank=False, max_length=30)

