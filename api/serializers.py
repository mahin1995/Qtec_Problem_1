from rest_framework import serializers
from .models import *

class keyword_Serializer(serializers.ModelSerializer):
    class Meta:
        model = keyword
        fields = ('__all__')

