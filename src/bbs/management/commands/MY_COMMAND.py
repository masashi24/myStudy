from django.core.management.base import BaseCommand, CommandError

from ...models import Article, Racer
from ...myRequests import sample
from ...forms import SearchForm
from ...forms import ArticleForm, RacerForm

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("registering data")
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