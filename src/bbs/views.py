from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Racer
from .myRequests import sample
from .forms import SearchForm
from .forms import ArticleForm, RacerForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    model = Article

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

def create(LoginRequiredMixin, request):
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

def update(LoginRequiredMixin, request, id):
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

def delete(LoginRequiredMixin, request, id):
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
    racerdata = Racer(victoryRatio=str(message["勝率"]), \
                      secondRatio=str(message["2連対率"]),\
                      thirdRatio=str(message["3連対率"]),\
                      raceNum=str(message["出走回数"]),\
                      finalJoinedNum=str(message["優出回数"]),\
                      victoryNum=str(message["優勝回数"]),\
                      startAvg=str(message["平均スタートタイミング"]),\
                      flyingNum=str(message["フライング回数"]),\
                      lateNum=str(message["出遅れ回数（選手責任）"]),\
                      Ability=str(message["能力指数"]),\
                      firstNum=str(message["1着"]),\
                      secondNum=str(message["2着"]),\
                      thirdNum=str(message["3着"]),\
                      fourthNum=str(message["4着"]),\
                      fivthNum=str(message["5着"]),\
                      sixthNum=str(message["6着"]))
    racerdata.save()

    context = {
        'message': message,
        'racerdata': racerdata,
        }
    return render(request, 'bbs/index.html', context)