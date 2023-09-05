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
    region = models.CharField(choices=REGION_CHOICES, null=False, blank=False, max_length=30)


class Counties(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    name = models.CharField(max_length=100, null=False, blank=False)
    state = models.ForeignKey(States, related_name='counties', on_delete=models.CASCADE)


class Neighborhoods(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    name = models.CharField(max_length=100, null=False, blank=False)
    county = models.ForeignKey(Counties, related_name='neighborhoods', on_delete=models.CASCADE)
