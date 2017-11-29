from django.shortcuts import render
from django.http import HttpResponse
import json
from django.forms.models import model_to_dict
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import datetime
from . import models

# Create your views here.


def index(request):
    return render(request, 'blog/index.html', {'title': 'DTL'})


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

    article = models.Article.objects.create(title=title, content=content)
    article = model_to_dict(article)
    articles = models.Article.objects.all()
    json_data = serializers.serialize("json", articles)
    dict_data = json.loads(json_data)
    result = {
        'code': 0,
        'ext': 'success',
        'article': article,
        'articles': dict_data}
    return HttpResponse(json.dumps(result, cls=DateEncoder, ensure_ascii=False))


def edit(request):
    article_id = request.GET.get('id', 0)
    title = request.GET.get('title', 'defaultTitle')
    content = request.GET.get('content', 'defaultContent')

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()

    result = {'code': 0, 'ext': 'success', 'article_id': article.id}
    return HttpResponse(json.dumps(result, ensure_ascii=False))


def delete(request):
    article_id = request.GET.get('id', 0)
    models.Article.objects.get(pk=article_id).delete()
    result = {'code': 0, 'ext': 'success'}
    return HttpResponse(json.dumps(result, ensure_ascii=False))


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)