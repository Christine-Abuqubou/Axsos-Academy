from django.shortcuts import render, redirect

def index(request):
    # Get the current visit count, default to 0 if not set
    count = request.session.get('visit_count', 0)
    count += 1

    # Store back into session
    request.session['visit_count'] = count

    context = {
        "count": count
    }
    return render(request, "index.html", context)


def destroy_session(request):
    # Clear all session data
    request.session.flush()
    return redirect('/')
