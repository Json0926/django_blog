from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request):
	articles = models.Article.objects.all()
	return render(request, 'blog/index.html', {'articles': articles})
#render第一个参数是本身request，第二个参数是模板位置，第三个是传递的数据

def article_page(request, article_id):
	article = models.Article.objects.get(pk=article_id)
	return render(request, 'blog/article_page.html', {'article': article})

def edit_page(request):
	title = request.POST.get('title', 'TITLE')
	content = request.POST.get('content', 'CONTENT')
	models.Article.objects.create(title=title, content=content)
	articles = models.Article.objects.all()
	return render(request, 'blog/index.html', {'articles': articles})