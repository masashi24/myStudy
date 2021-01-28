import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Article, Racer, Book
from .myRequests import sample
from .forms import SearchForm
from .forms import ArticleForm, RacerForm, BookForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import redirect

from django.contrib import messages

from .models import Store, Staff, Schedule


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

class RacerIndexView(generic.ListView):
    model = Racer

'''
class Scraping(generic.edit.CreateView):
    model = Racer
    fields = '__all__'
    template_name = 'scraping.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context
'''
#'''
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
    #'''

def newBook(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = Book()
            print(request)
            book.title = request.POST['title']
            book.link = request.POST['link']
            book.image = request.FILES['image']
            book.author = request.user
            book.published_date = timezone.now()
            book.save()
            return redirect('bbs:bookList')
    else:
        form = BookForm()
    return render(request, 'bbs/new.html', {'form': form})

def bookList(request):
    form = BookForm(request)
    book = Book.objects.order_by('published_date').reverse()

    context = {
        'message': 'book List',
        'books': book,
    }
    return render(request, 'bbs/bookList.html', context)

'''
def bookDetail(request, id):
    book = get_object_or_404(Book, pk=id)
    context = {
        'message': 'book Detail ' + str(id),
        'book': book,
    }
    return render(request, 'bbs/bookDetail.html', context) #'''


class bookDetail(generic.TemplateView):
    template_name = 'bbs/bookDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = get_object_or_404(Book, pk=self.kwargs['id'])
        owner = book.owner
        context = {
            'message': 'bbs:book Detail ' + str(self.kwargs['id']),
            'book': book,
        }
        today = datetime.date.today()
        user = self.request.user

        # どの日を基準にカレンダーを表示するかの処理。
        # 年月日の指定があればそれを、なければ今日からの表示。
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        if year and month and day:
            base_date = datetime.date(year=year, month=month, day=day)
        else:
            base_date = today

        # カレンダーは1週間分表示するので、基準日から1週間の日付を作成しておく
        days = [base_date + datetime.timedelta(days=day) for day in range(7)]
        start_day = days[0]
        end_day = days[-1]

        # 9時から17時まで1時間刻み、1週間分の、値がTrueなカレンダーを作る
        calendar = {}
        for hour in range(8, 18):
            row = {}
            for day in days:
                row[day] = True
            calendar[hour] = row

        # カレンダー表示する最初と最後の日時の間にある予約を取得する
        scheduleList = []
        start_time = datetime.datetime.combine(start_day, datetime.time(hour=9, minute=0, second=0))
        end_time = datetime.datetime.combine(end_day, datetime.time(hour=17, minute=0, second=0))
        for schedule in Schedule.objects.filter(target=owner).exclude(Q(start__gt=end_time) | Q(end__lt=start_time)): #exclude:レコードの除外/Q：条件に合うレコードのみまとめる（カプセル化）
            local_dt = timezone.localtime(schedule.start)
            booking_date = local_dt.date()
            booking_hour = local_dt.hour
            scheduleList.append(schedule)
            scheduleList.append(local_dt)
            scheduleList.append(booking_date)
            scheduleList.append(booking_hour)
            if booking_hour in calendar and booking_date in calendar[booking_hour]:
                calendar[booking_hour][booking_date] = False

        #context['staff'] = staff
        context['calendar'] = calendar
        context['days'] = days
        context['start_day'] = start_day
        context['end_day'] = end_day
        context['before'] = days[0] - datetime.timedelta(days=7)
        context['next'] = days[-1] + datetime.timedelta(days=1)
        context['today'] = today
        context['user'] = user
        context['scheduleList'] = scheduleList
        #context['public_holidays'] = settings.PUBLIC_HOLIDAYS
        return context #'''


    #return render(request, 'bbs/bookDetail.html', context)


class StoreList(generic.ListView):
    model = Store
    ordering = 'name'


class StaffList(generic.ListView):
    model = Staff
    ordering = 'name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['store'] = self.store
        return context

    def get_queryset(self):
        store = self.store = get_object_or_404(Store, pk=self.kwargs['pk'])
        queryset = super().get_queryset().filter(store=store)
        return queryset



class Booking(generic.CreateView):
    model = Schedule
    fields = ('name',)
    template_name = 'bbs/booking.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['staff'] = get_object_or_404(Staff, pk=self.kwargs['pk'])
        #book = get_object_or_404(Book, pk=self.kwargs['id'])
        return context

    def form_valid(self, form):
        #staff = get_object_or_404(Staff, pk=self.kwargs['pk'])
        book = get_object_or_404(Book, pk=self.kwargs['id'])
        target = book.owner
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        hour = self.kwargs.get('hour')
        start = datetime.datetime(year=year, month=month, day=day, hour=hour)
        end = datetime.datetime(year=year, month=month, day=day, hour=hour + 1)
        if Schedule.objects.filter(target=book.owner, start=start).exists():
            messages.error(self.request, 'すみません、入れ違いで予約がありました。別の日時はどうですか。')
        else:
            schedule = form.save(commit=False)
            #schedule.staff = staff
            schedule.start = start
            schedule.end = end
            schedule.target = target
            schedule.save()
        return redirect('bbs:bookList', pk=book.id, year=year, month=month, day=day)


'''
class StaffCalendar(generic.TemplateView):
    template_name = 'booking/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        staff = get_object_or_404(Staff, pk=self.kwargs['pk'])
        today = datetime.date.today()

        # どの日を基準にカレンダーを表示するかの処理。
        # 年月日の指定があればそれを、なければ今日からの表示。
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        if year and month and day:
            base_date = datetime.date(year=year, month=month, day=day)
        else:
            base_date = today

        # カレンダーは1週間分表示するので、基準日から1週間の日付を作成しておく
        days = [base_date + datetime.timedelta(days=day) for day in range(7)]
        start_day = days[0]
        end_day = days[-1]

        # 9時から17時まで1時間刻み、1週間分の、値がTrueなカレンダーを作る
        calendar = {}
        for hour in range(9, 18):
            row = {}
            for day in days:
                row[day] = True
            calendar[hour] = row

        # カレンダー表示する最初と最後の日時の間にある予約を取得する
        start_time = datetime.datetime.combine(start_day, datetime.time(hour=9, minute=0, second=0))
        end_time = datetime.datetime.combine(end_day, datetime.time(hour=17, minute=0, second=0))
        for schedule in Schedule.objects.filter(staff=staff).exclude(Q(start__gt=end_time) | Q(end__lt=start_time)):
            local_dt = timezone.localtime(schedule.start)
            booking_date = local_dt.date()
            booking_hour = local_dt.hour
            if booking_hour in calendar and booking_date in calendar[booking_hour]:
                calendar[booking_hour][booking_date] = False

        context['staff'] = staff
        context['calendar'] = calendar
        context['days'] = days
        context['start_day'] = start_day
        context['end_day'] = end_day
        context['before'] = days[0] - datetime.timedelta(days=7)
        context['next'] = days[-1] + datetime.timedelta(days=1)
        context['today'] = today
        context['public_holidays'] = settings.PUBLIC_HOLIDAYS
        return context #'''
