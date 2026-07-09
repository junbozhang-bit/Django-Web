from django.shortcuts import render
from rest_framework import generics
from .models import Course,Stage
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count
# Create your views here.

class ResultSetPagination(PageNumberPagination):
    '''
    自定义分页器
    '''
    page_query_param = 'page'
    page_size_query_param = 'size'
    page_size = 10

class CourseListView(generics.ListAPIView):
    # queryset = Course.objects.all()
    queryset = Course.objects.annotate(
        stage_count = Count('stages'),
        chapter_count = Count('stages__chapters'),
        section_count = Count('stages__chapters__sections')
    ).values(
        'id','name','brief','icon','learn_info','learn_style','learn_time','supervision','level',
        'stage_count','chapter_count','section_count'
    )
    serializer_class = CourseListSerializer

    #设置分页
    pagination_class = ResultSetPagination

class StageListView(generics.ListAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageListSerializer

    #设置数据过滤器
    filterset_fields = ('course',)

class ChapterListView(generics.ListAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterListSerializer

    # 设置数据过滤器
    filterset_fields = ('stage',)

class SectionListView(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionListSerializer

    # 设置数据过滤器
    filterset_fields = ('chapter',)

class StageDetailView(generics.RetrieveAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageDetailSerializer

