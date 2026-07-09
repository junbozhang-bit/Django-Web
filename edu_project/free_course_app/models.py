from django.db import models

from course_app.models import Stage
from teacher_app.models import Teacher


# Create your models here.
class FreeCourse(models.Model):
    price = models.IntegerField(blank=True, null=True,verbose_name='价格')
    img = models.CharField(blank=True,null=True,max_length=512,verbose_name='图片')

    start_time = models.DateTimeField(blank=True,null=True,verbose_name='开始时间')
    end_time = models.DateTimeField(blank=True,null=True,verbose_name='结束时间')

    stage = models.ForeignKey(Stage,related_name='free_courses',on_delete=models.CASCADE,verbose_name='课程阶段',null=True,blank=True)
    teacher = models.ForeignKey(Teacher,related_name='free_courses',on_delete=models.CASCADE,verbose_name='讲师',null=True,blank=True)


    class Meta:
        db_table = 't_free_course'
