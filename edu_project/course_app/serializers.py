from .models import *
from rest_framework import serializers

class CourseListSerializer(serializers.ModelSerializer):

    stage_count = serializers.IntegerField()
    chapter_count = serializers.IntegerField()
    section_count = serializers.IntegerField()

    class Meta:
        model = Course
        fields = '__all__'

class StageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'

class ChapterListSerializer(serializers.ModelSerializer):
    '''
    课程章节序列化器
    '''
    class Meta:
        model = Chapter
        fields = '__all__'


class SectionListSerializer(serializers.ModelSerializer):
    '''
    课程小节序列化器
    '''
    class Meta:
        model = Section
        fields = '__all__'

class ChapterDetailSerializer(serializers.ModelSerializer):
    '''
    课程章节详情序列化器
    '''
    sections = SectionListSerializer(many=True,read_only=True)
    class Meta:
        model = Chapter
        fields = '__all__'


class StageDetailSerializer(serializers.ModelSerializer):
    '''
    课程阶段详情序列化器
    '''
    chapters = ChapterDetailSerializer(many=True,read_only=True)
    class Meta:
        model = Stage
        fields = '__all__'

