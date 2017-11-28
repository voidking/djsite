from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    # 参数 auto_now=True 表示自动添加隐藏的时间
    pub_time = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return self.title
