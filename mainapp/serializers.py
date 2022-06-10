from dataclasses import field
from statistics import mode
from rest_framework import serializers
from .models import plan

class Myplanserializers(serializers.ModelSerializer):
    class Meta:
        model=plan
        fields=['pk','items']

