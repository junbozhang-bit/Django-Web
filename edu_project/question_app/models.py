from django.db import models

from user_app.models import User
from course_app.models import Section

class Question(models.Model):
    title = models.CharField(null = True,blank=True,max_length=200,verbose_name='问题标题')
    content = models.TextField(null = True,blank=True, verbose_name='问题内容')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    section = models.ForeignKey(Section,on_delete=models.CASCADE,verbose_name='章节')
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='提问者/回答者')
    answers = models.ForeignKey(
                    'self',on_delete=models.CASCADE,
                    verbose_name='回答',null=True,blank=True,related_name='children'
                    )

    class Meta:
        db_table = 't_question'  
