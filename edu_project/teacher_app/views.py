from django.shortcuts import render
from rest_framework import generics
from .serializers import TeacherListSerializer
from .models import Teacher
# Create your views here.
class TeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer