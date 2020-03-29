from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns =[
    path('sinup/', views.SignUpView.as_view(), name='signup')
]