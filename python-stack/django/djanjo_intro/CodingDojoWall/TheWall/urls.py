from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_message', views.post_message),
    
    
]