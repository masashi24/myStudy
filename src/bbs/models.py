from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    content = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.content

class Racer(models.Model):
    victoryRatio = models.CharField(max_length = 10)
    secondRatio = models.CharField(max_length = 10)
    thirdRatio = models.CharField(max_length = 10)
    raceNum = models.CharField(max_length = 10)
    finalJoinedNum = models.CharField(max_length = 10)
    victoryNum = models.CharField(max_length = 10)
    startAvg = models.CharField(max_length = 10)
    flyingNum = models.CharField(max_length = 10)
    lateNum = models.CharField(max_length = 10)
    Ability = models.CharField(max_length = 10)
    firstNum = models.CharField(max_length = 10)
    secondNum = models.CharField(max_length = 10)
    thirdNum = models.CharField(max_length = 10)
    fourthNum = models.CharField(max_length = 10)
    fivthNum = models.CharField(max_length = 10)
    sixthNum = models.CharField(max_length = 10)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

