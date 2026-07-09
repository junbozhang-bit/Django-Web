from rest_framework import serializers
from .models import UpdateCourse

class UpdateCourseListSerializer(serializers.ModelSerializer):

    create_time = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = UpdateCourse
        fields = ['id','name','create_time','update_type']

class UpdateCourseDetailSerializer(serializers.ModelSerializer):

    course_name = serializers.CharField(source='course.name')
    stage_name = serializers.CharField(source='stage.name')

    class Meta:
        model = UpdateCourse
        fields = '__all__'