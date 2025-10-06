
from django.shortcuts import render, redirect
import random

def index(request):
    # Initialize game
    if 'number' not in request.session or 'reset' in request.GET:
        request.session['number'] = random.randint(1, 100)
        request.session['attempts'] = 0
        request.session['status'] = ""
        request.session['game_over'] = False
        if 'reset' in request.GET:
            del request.session['reset']

    leaderboard = request.session.get('leaderboard', [])
    
    return render(request, 'index.html', {
        'status': request.session.get('status', ""),
        'attempts': request.session.get('attempts', 0),
        'game_over': request.session.get('game_over', False),
        'leaderboard': leaderboard
    })

def guess(request):
    if request.method == 'POST' and not request.session.get('game_over', False):
        guess = int(request.POST.get('guess'))
        number = request.session['number']
        attempts = request.session.get('attempts', 0) + 1
        request.session['attempts'] = attempts

        # Max 5 attempts
        if attempts >= 5 and guess != number:
            request.session['status'] = f"You Lose! The number was {number}."
            request.session['game_over'] = True
        elif guess < number:
            request.session['status'] = "Too Low!"
        elif guess > number:
            request.session['status'] = "Too High!"
        else:
            request.session['status'] = f"Correct! You guessed it in {attempts} attempts."
            request.session['game_over'] = True
            # Save leaderboard in session
            leaderboard = request.session.get('leaderboard', [])
            leaderboard.append({'attempts': attempts})
            request.session['leaderboard'] = leaderboard

        return redirect('index')
    return redirect('index')

def reset(request):
    request.session['reset'] = True
    return redirect('index')
