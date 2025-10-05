
from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []

    # ✅ Add this list
    locations = ['farm', 'cave', 'house', 'Quest']
    

    return render(request, 'index.html', {
        'gold': request.session['gold'],
        'activities': request.session['activities'],
        'locations': locations  # Pass it to the template
    })

    

def process_money(request):
    if request.method == 'POST':
        location = request.POST['location']
        gold = 0

        if location == 'farm':
            gold = random.randint(10, 20)
        elif location == 'cave':
            gold = random.randint(5, 10)
        elif location == 'house':
            gold = random.randint(2, 5)
        elif location == 'quest':
            gold = random.randint(-50, 50)

        # Update gold
        request.session['gold'] += gold

        # Format activity message
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        result = f"Earned {gold} gold" if gold >= 0 else f"Lost {abs(gold)} gold"
        message = f"{time} - You entered the {location} and {result}."

        # Add color tag for styling
        activity = {
            'message': message,
            'color': 'green' if gold >= 0 else 'red'
        }

        request.session['activities'].insert(0, activity)
        request.session.modified = True

    return redirect('index')
