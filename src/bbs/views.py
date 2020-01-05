from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Racer
from .myRequests import sample
from .forms import SearchForm
from .forms import ArticleForm, RacerForm

# Create your views here.

def index(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        articles = Article.objects.filter(content__contains=keyword)
    else:
        searchForm = SearchForm()
        articles = Article.objects.all()

    context = {
        'message': 'Welcome my BBS',
        'articles': articles,
        'searchForm': searchForm,
        }
    return render(request, 'bbs/index.html', context)

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    context = {
        'message': 'Show Article ' + str(id),
        'article': article,
        }
    return render(request, 'bbs/detail.html', context)

def new(request):
    articleForm = ArticleForm()

    context = {
        'message': 'New Article',
        'articleForm': articleForm,
    }

    return render(request, 'bbs/new.html', context)

def create(request):
    if request.method == 'POST':
        articleForm = ArticleForm(request.POST)
        if articleForm.is_valid():
            article = articleForm.save()
    
    context = {
        'message': 'Create article' + str(article.id),
        'article': article
        }
    return render(request, 'bbs/detail.html', context)

def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    articleForm = ArticleForm(instance=article)

    context = {
        'message': 'Edit Article',
        'article': article,
        'articleForm': articleForm,
    }
    return render(request, 'bbs/edit.html', context)

def update(request, id):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=id)
        articleForm = ArticleForm(request.POST, instance=article)
        if articleForm.is_valid():
            articleForm.save()
    context = {
        'message': 'Update article ' + str(id),
        'article': article,
    }
    return render(request, 'bbs/detail.html', context)

def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()

    articles = Article.objects.all()
    context = {
        'message': 'Deleted article' + str(id),
        'articles': articles,
        }
    return render(request, 'bbs/index.html', context)

def scraping(request):
    message = sample.myScraping()
    racerdata = Racer(victoryRatio = '1')
    racerdata.save()

    context = {
        'message': message,
        'racerdata': racerdata,
        }
    return render(request, 'bbs/scraping.html', context)