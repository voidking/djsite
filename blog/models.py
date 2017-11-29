from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    # 参数 auto_now=True 表示自动添加隐藏的时间
    pub_time = models.DateTimeField('发布日期', default=timezone.now)

    def __str__(self):
        return self.title
