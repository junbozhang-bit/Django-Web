from django.db import models

from user_app.models import User
from course_app.models import Course,Section

# 用于个人订阅课程的模型
class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_course',verbose_name='用户')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='user_course',verbose_name='课程')

    class Meta:
        db_table = 't_user_course'

# 用于个人收藏课程的模型
class UserSection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_section',verbose_name='用户')
    section = models.ForeignKey(Section, on_delete=models.CASCADE,related_name='user_section',verbose_name='课程小节')

    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    class Meta:
        db_table = 't_user_section'