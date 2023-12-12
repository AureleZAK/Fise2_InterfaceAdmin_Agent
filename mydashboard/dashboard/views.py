from django.shortcuts import render

# Create your views here.
# dashboard/views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import ServerData
import plotly.express as px
import pandas as pd
from src import count_log

def dashboard(request):
    data_points = ServerData.objects.all()  # Récupérez les données depuis la base de données
    return render(request, 'dashboard/dashboard.html', {'data_points': data_points})

def home(request):
    return render(request, 'dashboard/home.html')
def my_view(request):
    # votre logique de vue ici
    return HttpResponse("Hello, this is my view!")
# views.py

# views.py



def pie_chart(request):
    # Fake values for the pie chart (replace with your own data)

    result, good, error, pagetotest = count_log("src/tests/filelog.txt")

    labels = [200, 404]

    values = [good, error]

    # Create a Pandas DataFrame
    data = {'labels': labels, 'values': values}
    df = pd.DataFrame(data)

    # Create the pie chart with Plotly Express
    fig = px.pie(df, names='labels', values='values', title='Pie Chart')

    # Convert the chart to HTML
    graph_html = fig.to_html(full_html=False)

    # Render the page with the chart
    return render(request, 'dashboard/pie_chart.html', {'graph_html': graph_html})

