from rest_framework import serializers
from .models import UserCourse,UserSection

class UserCourseNameListSerializer(serializers.ModelSerializer):
    '''
    获取用户订阅课程 名称
    '''
    id = serializers.IntegerField(source='course.id')
    course_name = serializers.CharField(source='course.name')

    class Meta:
        model = UserCourse
        fields = ('id','course_name')

class UserCourseListSerializer(serializers.ModelSerializer):
    '''
    获取用户订阅课程
    '''
    id = serializers.IntegerField(source='course.id')
    course_name = serializers.CharField(source='course.name')
    icon = serializers.CharField(source='course.icon')

    class Meta:
        model = UserCourse
        fields = ('id','course_name','icon')

class MySectionListSerializer(serializers.ModelSerializer):
    '''
        获取用户收藏课程的信息，用于个人中心
    '''
    id = serializers.IntegerField(source='section.id')
    section_name = serializers.CharField(source='section.name')
    section_duration = serializers.CharField(source='section.duration')
    section_learn_count = serializers.CharField(source='section.learned_count')

    create_time = serializers.DateTimeField(format="%Y-%m")

    class Meta:
        model = UserSection
        fields = '__all__'

class UserAddSectionSerializer(serializers.ModelSerializer):
    '''
    用户增加收藏
    '''
    section = serializers.IntegerField(required=True)

    class Meta:
        model = UserSection
        fields = ('section',)

from order_app.models import Order
class OrderListSerializer(serializers.ModelSerializer):

    gmt_payment = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    course_name = serializers.CharField(source='course.name')
    class_type_name = serializers.CharField(source='class_type.name')

    class Meta:
        model = Order
        fields = '__all__'