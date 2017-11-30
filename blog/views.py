from django.shortcuts import render
from django.http import HttpResponse
import json
from django.forms.models import model_to_dict
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import datetime
import time
from django.utils import timezone
from django.db.models import Q
from . import models

# Create your views here.


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def hello(request):
    return HttpResponse('helloworld')


def list(request):
    articles = models.Article.objects.all()
    article = models.Article.objects.get(pk=1)
    return render(request, 'blog/list.html',
                  {'articles': articles, 'article': article})


@csrf_exempt
def add(request):
    title = request.POST.get('title', 'defaultTitle')
    content = request.POST.get('content', 'defaultContent')

    pub_time = utc2local(timezone.now())
    LOCAL_FORMAT = "%Y-%m-%d %H:%M:%S"
    pub_time = pub_time.strftime(LOCAL_FORMAT)

    models.Article.objects.create(
        title=title,
        content=content,
        pub_time=pub_time)

    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


@csrf_exempt
def edit(request):
    article_id = request.POST.get('id', 0)
    title = request.POST.get('title', 'defaultTitle')
    content = request.POST.get('content', 'defaultContent')
    pub_time = utc2local(timezone.now())
    LOCAL_FORMAT = "%Y-%m-%d %H:%M:%S"
    pub_time = pub_time.strftime(LOCAL_FORMAT)

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.pub_time = pub_time
    article.save()

    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


@csrf_exempt
def delete(request):
    article_id = request.POST.get('id', 0)
    models.Article.objects.get(pk=article_id).delete()
    result = {'code': 0, 'ext': 'success'}
    return HttpResponse(json.dumps(result, ensure_ascii=False))


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def detail(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article.html',
                  {'article': article})


def toadd(request):
    return render(request, 'blog/add.html')


def toedit(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit.html', {'article': article})


@csrf_exempt
def search(request):
    key = request.POST.get('key')
    articles = models.Article.objects.filter(Q(title__contains=key) | Q(content__contains=key))
    json_data = serializers.serialize("json", articles)
    dict_data = json.loads(json_data)
    result = {
        'code': 0,
        'ext': 'success',
        'articles': dict_data}
    return HttpResponse(json.dumps(result, ensure_ascii=False))


def utc2local(utc_st):
    # UTC时间转本地时间（+8:00）
    now_stamp = time.time()
    local_time = datetime.datetime.fromtimestamp(now_stamp)
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st
