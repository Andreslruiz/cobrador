from django.urls import path

from . import views

app_name = 'common'

urlpatterns = [
    path('send-daily-report/', views.send_daily_report, name='send_daily_report')
]
