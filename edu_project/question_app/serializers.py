from rest_framework import serializers
from .models import Question

class QuestionAddSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    content = serializers.CharField(max_length=1000,allow_blank=True,allow_null=True)
    section = serializers.IntegerField()

    class Meta:
        model = Question
        fields = ['title','content','section']

class AnswerSerializer(serializers.ModelSerializer):
    content = serializers.CharField(max_length=1000,allow_blank=True,allow_null=True)
    question = serializers.IntegerField()
    section = serializers.IntegerField()

    class Meta:
        model = Question
        fields = ['id','content','question','section']

# 获取问题列表序列化器
class QuestionListSerializer(serializers.ModelSerializer):
    # 获取问题所在哪个课程分类
    course_name = serializers.CharField(source='section.chapter.stage.course.name')
    # 获取问题所在哪个课程阶段
    stage_name = serializers.CharField(source='section.chapter.stage.name')
    # 获取问题所在哪个课程章节
    chapter_name = serializers.CharField(source='section.chapter.name')
    # 获取问题所在哪个课程小节
    section_name = serializers.CharField(source='section.name')
    # 设置格式化
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    
    class Meta:
        model = Question
        fields = '__all__'

class AnswerDetailSerializer(serializers.ModelSerializer):
    # 获取用户的昵称
    user_name = serializers.CharField(source='user.nickname')
    # 设置格式化
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    # 设置回答问题的序列化器
    class Meta:
        model = Question
        fields = ['user_name','content','create_time']


class QuestionDetailSerializer(serializers.ModelSerializer):
    # 获取用户的昵称
    user_name = serializers.CharField(source='user.nickname')
    # 获取问题所在哪个课程分类
    course_name = serializers.CharField(source='section.chapter.stage.course.name')
    # 获取问题所在哪个课程阶段
    stage_name = serializers.CharField(source='section.chapter.stage.name')
    # 获取问题所在哪个课程章节
    chapter_name = serializers.CharField(source='section.chapter.name')
    # 获取问题所在哪个课程小节
    section_name = serializers.CharField(source='section.name')
    # 设置格式化
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    # 设置回答问题的序列化器
    answers = AnswerDetailSerializer(many=True,read_only=True,source='children')
    class Meta:
        model = Question
        fields = '__all__'