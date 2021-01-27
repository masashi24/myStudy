from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('bbs:detail', kwargs={'pk': self.pk})

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

class Book(models.Model):
    author = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media/',blank=True, null=True)
    title = models.CharField(max_length=32)
    link = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)


    start = models.DateTimeField('開始時間',null=True)
    end = models.DateTimeField('終了時間',null=True)
    name = models.CharField('予約者名', max_length=255,null=True)
    #staff = models.ForeignKey('Staff', verbose_name='スタッフ', on_delete=models.CASCADE,null=True)

    def __str__(self):
        start = timezone.localtime(self.start).strftime('%Y/%m/%d %H:%M:%S')
        end = timezone.localtime(self.end).strftime('%Y/%m/%d %H:%M:%S')
        #return f'{self.name} {start} ~ {end} {self.staff}'
        return f'{self.name} {start} ~ {end}'


    def publish(self):
        self.published_date = timezone.now()
        self.save()




class Store(models.Model):
    """店舗"""
    name = models.CharField('店名', max_length=255)

    def __str__(self):
        return self.name

class Staff(models.Model):
    """店舗スタッフ"""
    name = models.CharField('表示名', max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='ログインユーザー', on_delete=models.CASCADE
    )
    store = models.ForeignKey(Store, verbose_name='店舗', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'store'], name='unique_staff'),
        ]

    def __str__(self):
        return f'{self.store.name} - {self.name}'

class Schedule(models.Model):
    """予約スケジュール."""
    start = models.DateTimeField('開始時間')
    end = models.DateTimeField('終了時間')
    name = models.CharField('予約者名', max_length=255)
    staff = models.ForeignKey('Staff', verbose_name='スタッフ', on_delete=models.CASCADE)

    def __str__(self):
        start = timezone.localtime(self.start).strftime('%Y/%m/%d %H:%M:%S')
        end = timezone.localtime(self.end).strftime('%Y/%m/%d %H:%M:%S')
        return f'{self.name} {start} ~ {end} {self.staff}'
