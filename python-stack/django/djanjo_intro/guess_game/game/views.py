
from django.shortcuts import render, redirect
import random

def index(request):
    # Initialize random number
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
        request.session['message'] = ""

    if request.method == 'POST':
        guess = request.POST.get('guess')
        if guess:
            guess = int(guess)
            target = request.session['number']
            if guess < target:
                request.session['message'] = "Too low!"
            elif guess > target:
                request.session['message'] = "Too high!"
            else:
                request.session['message'] = f"Correct! It was {target} 🎉"

    return render(request, 'index.html', {
        'message': request.session.get('message', '')
    })


def reset(request):
    request.session.flush()
    return redirect('index')
