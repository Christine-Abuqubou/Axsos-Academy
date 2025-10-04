from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('destroy_session', views.destroy_session, name="destroy"),
    path('plus2', views.increment_two, name="plus2"),
    path('increment', views.increment_custom, name="increment"),
]

