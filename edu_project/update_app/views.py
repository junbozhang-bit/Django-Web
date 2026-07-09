from django.shortcuts import render
from .models import UpdateCourse
from .serializers import UpdateCourseListSerializer,UpdateCourseDetailSerializer
from rest_framework import generics
# Create your views here.
class UpdateCourseListView(generics.ListAPIView):
    queryset = UpdateCourse.objects.all().order_by('-create_time')
    serializer_class = UpdateCourseListSerializer

class UpdateCourseDetailView(generics.RetrieveAPIView):
    queryset = UpdateCourse.objects.all()
    serializer_class = UpdateCourseDetailSerializer