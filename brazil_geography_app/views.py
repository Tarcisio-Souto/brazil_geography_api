from django.shortcuts import render

from brazil_geography_app.serializers import StatesSerializer
from rest_framework import viewsets, permissions
from brazil_geography_app.models import States


class StatesViewSet(viewsets.ModelViewSet):
  queryset = States.objects.all()
  serializer_class = StatesSerializer
  permission_classes = [permissions.IsAuthenticated]
