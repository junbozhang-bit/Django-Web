from django.shortcuts import render
from .serializers import PlanDetailSerializer,ClassTypeListSerializer
from .models import Plan,ClassType
from rest_framework import generics
# Create your views here.
class PlanDetailView(generics.ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanDetailSerializer

    filterset_fields = ['course']

class ClassTypeListView(generics.ListAPIView):
    queryset = ClassType.objects.all()
    serializer_class = ClassTypeListSerializer

    filterset_fields = ['course']