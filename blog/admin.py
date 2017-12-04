from django.contrib import admin
from . import models

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    # 显示在admin控制台中的列名
    list_display = ('title', 'content', 'pub_time')
    # 时间过滤器
    list_filter = ('pub_time',)


admin.site.register(models.Article, ArticleAdmin)
