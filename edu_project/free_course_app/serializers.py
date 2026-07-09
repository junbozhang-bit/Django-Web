from rest_framework import serializers
from .models import FreeCourse

class FreeCourseListSerializer(serializers.ModelSerializer):

    stage_name = serializers.CharField(source='stage.name')
    teacher_name = serializers.CharField(source='teacher.name')
    #format格式化时间
    start_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    end_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = FreeCourse
        fields = '__all__'