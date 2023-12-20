# dashboard/urls.py

from django.urls import path
from .views import my_view, pie_chart, dashboard, home, get_api_data
from django.urls import path


urlpatterns = [
    path('pie_chart/', pie_chart, name='pie_chart'),
    path('home/', home, name='home' ),
    path('get_api_data/', get_api_data, name='get_api_data'),
    # autres patterns d'URL ici
]
