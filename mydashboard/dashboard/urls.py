# dashboard/urls.py

from django.urls import path
from .views import my_view, pie_chart, dashboard

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('my-view/', my_view, name='my_view'),
    path('pie_chart/', pie_chart, name='pie_chart'),
    # autres patterns d'URL ici
]
