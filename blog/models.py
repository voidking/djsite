from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    # pub_time = models.DateTimeField('发布日期', default=timezone.now)
    pub_time = models.CharField(max_length=64, default='')

    def __str__(self):
        return self.title