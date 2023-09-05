from rest_framework import serializers
from brazil_geography_app.models import States


class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = [
          'id',
          'name',
          'region']
