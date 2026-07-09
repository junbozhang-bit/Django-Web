from django.db import models

# Create your models here.
class RotationChart(models.Model):
    name = models.CharField(max_length=20, verbose_name='轮播图名称')
    img = models.CharField(max_length=255, verbose_name='轮播图图片')

    class Meta:
        db_table = 't_rotation_chart'

from django.db import models

class FeatureService(models.Model):
    name = models.CharField(max_length=20, verbose_name='服务特色名称')
    
    class Meta:
        db_table = 't_feature_service'
