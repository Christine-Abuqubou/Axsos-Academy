from django.contrib import admin
from django.urls import path
from game import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reset/', views.reset, name='reset'),
    path('admin/', admin.site.urls),
]
