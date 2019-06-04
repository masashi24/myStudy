from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article
from .myRequests import sample

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'message': 'Welcome my BBS',
        'articles': articles,
        }
    return render(request, 'bbs/index.html', context)

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    context = {
        'message': 'Show Article ' + str(id),
        'article': article,
    }
    return render(request, 'bbs/detail.html', context)

def scraping(request):
    #articles = Article.objects.all()
    message = sample.myScraping()
    context = {
        'message': message
        }
    return render(request, 'bbs/index.html', context)