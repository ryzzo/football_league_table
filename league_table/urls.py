from django.urls import path
from . import views

app_name = 'league_table'

urlpatterns = [
    path('', views.statsTable, name='stats_table'),
    path('table/', views.enterStat, name='enter_stats')
]