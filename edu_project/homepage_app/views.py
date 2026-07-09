from django.shortcuts import render
from rest_framework import generics
from .serializers import RotationChartListSerializer,FeatureServiceListSerializer
from .models import RotationChart,FeatureService
# Create your views here.
class RotationChartListView(generics.ListAPIView):
    queryset = RotationChart.objects.all().order_by('id')
    serializer_class = RotationChartListSerializer

class FeatureServiceListView(generics.ListAPIView):
    queryset = FeatureService.objects.all().order_by('-id')
    serializer_class = FeatureServiceListSerializer    