from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Racer
from .myRequests import sample
from .forms import SearchForm
from .forms import ArticleForm, RacerForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.

class IndexView(generic.ListView):
    model = Article

class DetailView(generic.DetailView):
    model = Article

class CreateView(generic.edit.CreateView):
    model = Article
    fields = '__all__'

class UpdateView(generic.edit.UpdateView):
    model = Article
    fields = '__all__'


class DeleteView(generic.edit.DeleteView):
    model = Article
    success_url = reverse_lazy('bbs:index')


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
    return render(request, 'bbs/scraping.html', context)