from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add_course',views.add_course,name='add_course'),
    # path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
    path('destroy/<int:course_id>/',views.destroy,name='destroy'),
    path('delete/<int:course_id>/', views.confirm_delete_course, name='delete_course'),
]