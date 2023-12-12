# dashboard/urls.py

from django.urls import path
from .views import my_view, pie_chart, dashboard, home
from django.urls import path


urlpatterns = [
    path('pie_chart/', pie_chart, name='pie_chart'),
    path('home/', home, name='home' ),
    # autres patterns d'URL ici
]
