from django.shortcuts import render, redirect

def index(request):
    # track total visits
    visits = request.session.get('visits', 0)
    visits += 1
    request.session['visits'] = visits

    # track counter
    counter = request.session.get('counter', 0)

    context = {
        "visits": visits,
        "counter": counter,
    }
    return render(request, "index.html", context)


def destroy_session(request):
    request.session.flush()  # clears all session data
    return redirect('/')


# NINJA BONUS: increment by +2
def increment_two(request):
    counter = request.session.get('counter', 0)
    counter += 2
    request.session['counter'] = counter
    return redirect('/')


# SENSEI BONUS: increment by custom value
def increment_custom(request):
    if request.method == "POST":
        try:
            val = int(request.POST.get("increment", 1))
        except ValueError:
            val = 1
        counter = request.session.get('counter', 0)
        counter += val
        request.session['counter'] = counter
    return redirect('/')
