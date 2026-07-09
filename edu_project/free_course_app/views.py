from django.shortcuts import render
from .serializers import FreeCourseListSerializer
from rest_framework import generics
from .models import FreeCourse
# Create your views here.
class FreeCourseListView(generics.ListAPIView):
    queryset = FreeCourse.objects.all()
    serializer_class = FreeCourseListSerializer