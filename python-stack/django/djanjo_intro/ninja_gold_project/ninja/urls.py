from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('process_money', views.process_money, name='process_money'),  # POST route
]
