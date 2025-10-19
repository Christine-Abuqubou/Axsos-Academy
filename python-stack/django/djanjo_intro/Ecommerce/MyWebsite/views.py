from django.shortcuts import render, redirect, HttpResponse
from . import models
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from . import models
from .models import Game

def index(request):
    context = {
    'current_year': datetime.now().year
    }
    return render(request , 'index.html',context)

def create_user_form(request):
    if request.method == 'POST':
        errors = models.User.objects.basic_validator_reg(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            print("Errors") 
            return redirect('/')    
        else:
            new_user = models.create_user(request.POST)
            request.session['user_id'] = new_user.id
            return redirect('/dashboard')
    else:
        return render(request, 'index.html')
    
def login_user_form(request):
        if request.method == 'POST':
            errors = models.User.objects.basic_validator_login(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                    print("Errors") 
                    return redirect('/')  
            else:
                user = models.login_user(request)
                if (user):
                    return redirect('/dashboard')
                else:
                    return render(request, 'index.html')
        else:
            return render(request, 'index.html')
        
        
def logout_form(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        return redirect('/')
    else:
        return redirect('/')
            
def view_user(request):
    if 'user_id' in request.session:
        context = {
            'user' : models.get_user(request.session['user_id']),
            'current_year': datetime.now().year
        }
        return render(request, 'viewuser.html' ,context)
    else:
        return redirect('/') 

def display_dashboard(request):
    if 'user_id' in request.session:
        context = {
             'games' : models.get_games(),
            'current_year': datetime.now().year
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('/')
    
def create_game(request):
    if 'user_id' in request.session:
        context = {
        'current_year': datetime.now().year
        }
        return render(request, 'creategame.html', context)
    else:
        return redirect('/') 
    
def creategameform(request):
    if request.method == 'POST':
        if  'user_id' in request.session:
            errors = models.Game.objects.basic_validator_save_Game(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                print("Errors") 
                return redirect('/creategame')  
            else:  
                models.create_game(request)
                return redirect('/dashboard')
        else: 
            return redirect('/')
    else:
        return render(request, 'index.html') 

def update_game(request, id):
    if 'user_id' in request.session:
        context = {
            'game' : models.get_game(id),
            'current_year': datetime.now().year
        }
        return render(request, 'updategame.html' ,context)
    else:
        return redirect('/')
def update_game_form(request):
    if request.method == 'POST':
        if  'user_id' in request.session:
            errors = models.Game.objects.basic_validator_save_Game(request.POST)      
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                print("Errors") 
                return redirect('/updategame/'+request.POST['gameid'])    
            else:
                models.update_game(request.POST)
                return redirect('/dashboard')
#         # else:
#         #     return redirect('/')
#     else:
#         return render(request, 'index.html')
    


def view_game(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    
    user_id = request.session['user_id']
    game = models.get_game(id)
    
    liked_games = models.liked_games(user_id)
    
    context = {
        'game': game,
        'liked_games': liked_games,
        'current_year': datetime.now().year,
    }
    return render(request, 'viewgame.html', context)


    
def delete_game_form(request):
    if request.method == 'POST':
        if  'user_id' in request.session:
            game_id = request.POST['gameid']
            user_id = request.POST['userid']
            if request.session['user_id'] == int(user_id):
                models.delete_game(game_id)
                return redirect('/dashboard')
            else:
                print("test")
                return render(request, 'index.html')
        else:
            return redirect('/')
    else:
        return render(request, 'index.html')

def edit_game_form(request):
    if request.method == 'POST':
        if  'user_id' in request.session:
            game_id = request.POST['gameid']
            user_id = request.POST['userid']
            if request.session['user_id'] == int(user_id):
                return redirect('/editgame/'+game_id)
            else:
                print("test")
                return render(request, 'updategame.html')
        else:
            return redirect('/')
    else:
        return render(request, 'index.html')



def favoriteGame(request,user_id,game_id):
    if request.method == 'POST':
        models.favorite_game(user_id,game_id)
        print(request.POST)
        print(user_id,game_id)
        return redirect(f'/viewgame/{game_id}')
    return redirect('/dashboard')

def like_game(request, game_id):
    if request.method == 'POST':
        models.liked_games(request.session['user_id'], game_id)
        return redirect(f'/viewgame/{game_id}')
    return redirect('/dashboard')


    
    
    
    
    




