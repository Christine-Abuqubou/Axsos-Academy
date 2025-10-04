from django.urls import path
from Main import views

urlpatterns = [
    path("", views.index,name="index"),
    path("destroy", views.destroy,name="destroy"),
    path("increment_2", views.increment_2,name="increment_2"),
    path("increment_custom", views.increment_custom,name="increment_custom")
    
]
