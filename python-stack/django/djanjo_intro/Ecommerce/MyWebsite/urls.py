from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard' , views.display_dashboard),
    path('createuserform' , views.create_user_form),
    
    path('loginuserform' , views.login_user_form),
    path('creategame' , views.create_game),
    path('viewuser' , views.view_user),
    path('logout' , views.logout_form),
    path('favorite/<int:user_id>/<int:game_id>', views.favoriteGame),

    path('creategameform' , views.creategameform),  
    path('editgame/<int:id>' , views.update_game),   
    path('viewgame/<int:id>' , views.view_game),   
    path('updategameform/<int:id>/', views.update_game_form, name='updategameform'),

    path('editgameform' , views.edit_game_form),
    path('like/<int:game_id>', views.like_game, name='like_game'),

    
    
]