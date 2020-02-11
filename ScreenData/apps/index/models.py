from django.db import models


class DataAll(models.Model):
    id = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=100, verbose_name="城市名")
    confirmedCount = models.IntegerField(verbose_name="确诊病例数")
    curedCount = models.IntegerField(verbose_name="治愈病例数")
    deadCount = models.IntegerField(verbose_name="死亡病例数")
    province_name = models.CharField(max_length=100, validators="省份")
    date_info = models.CharField(max_length=100, validators="日期")
    detail_time = models.CharField(max_length=100, validators="详细时间")
    cycle = models.IntegerField(validators="循环次数")

    def __str__(self):
        return self.cityName

    class Meta:
        db_table = 'data_all'
        verbose_name_plural = "疫情数据"
