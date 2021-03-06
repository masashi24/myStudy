from django.urls import path
from . import views

app_name = 'bbs'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('create', views.CreateView.as_view(), name='create'),
    path('<int:pk>/update', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.DeleteView.as_view(), name='delete'),

    path('racer', views.RacerIndexView.as_view(), name='racer'),
    path('scraping', views.scraping, name='scraping'),

    path('newbook', views.newBook, name='newBook'),
    path('bookList', views.bookList, name='bookList'),
    #path('bookList/<int:id>', views.bookDetail, name='bookDetail'),
    path('bookList/<int:id>', views.bookDetail.as_view(), name='bookDetail'),
    path('bookList/<int:id>/<int:year>/<int:month>/<int:day>/', views.bookDetail.as_view(), name='bookDetail'),

    path('store_list', views.StoreList.as_view(), name='store_list'),
    path('store/<int:pk>/staffs/', views.StaffList.as_view(), name='staff_list'),

    path('bookList/<int:id>/booking/<int:year>/<int:month>/<int:day>/<int:hour>/', views.Booking.as_view(), name='booking'),

    #path('staff/<int:pk>/calendar/', views.StaffCalendar.as_view(), name='calendar'),
    #path('staff/<int:pk>/calendar/<int:year>/<int:month>/<int:day>/', views.StaffCalendar.as_view(), name='calendar'),
]