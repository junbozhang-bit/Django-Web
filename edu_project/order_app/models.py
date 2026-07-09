from django.db import models

from user_app.models import User
from course_app.models import Course
from plan_app.models import ClassType

class Order(models.Model):
    ORDER_TYPE = (
        (0, '未支付'),
        (1, '已支付')
    )

    id = models.CharField(primary_key=True, max_length=32)
    order_type = models.IntegerField(choices=ORDER_TYPE,default=0,verbose_name='订单状态')
    amount = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True,verbose_name='订单金额')
    total_amount = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True,verbose_name='实际支付金额')
    gmt_payment = models.DateTimeField(blank=True,null=True,verbose_name='支付时间')

    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='用户')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,verbose_name='课程')
    class_type = models.ForeignKey(ClassType, on_delete=models.CASCADE,verbose_name='班级类型')

    class Meta:
        db_table = 't_order'
