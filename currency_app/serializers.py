from rest_framework import serializers
from .models import Currency_detail

class ConvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency_detail
        fields = '__all__'