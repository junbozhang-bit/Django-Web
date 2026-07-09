from rest_framework import serializers
from .models import RotationChart,FeatureService

class RotationChartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RotationChart
        fields = '__all__'

class FeatureServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureService
        fields = '__all__'