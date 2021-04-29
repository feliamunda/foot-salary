from django.urls import path

from . import views

app_name = 'calculator'

# This array manage wich view will manage each endpoint 
urlpatterns = [
    path('', views.CalculatorView.as_view(),name='calculate_team_salary'),
]