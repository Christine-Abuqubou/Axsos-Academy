from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Show


def home(request):
    return redirect('/shows')


def all_shows(request):
    shows = Show().get_all()
    return render(request, "index.html", {"shows": shows})


def new_show(request):
    return render(request, "new.html")


def create_show(request):
    if request.method == "POST":
        show, errors = Show.objects.create(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/shows/new")
        return redirect(f"/shows/{show.id}")
    return redirect("/shows/new")
    # if request.method == "POST":
    #     show = Show().create(request.POST)
    #     return redirect(f"/shows/{show.id}")
    # return redirect("/shows/new")


def show_detail(request, show_id):
    show = Show().get_one(show_id)
    if not show:
        return redirect('/shows')
    return render(request, "show.html", {"show": show})


def edit_show(request, show_id):
    if request.method == "POST":
        show = Show.objects.get(id=show_id)  
        updated_show, errors = Show.objects.update_show(show, request.POST)
        
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{show_id}/edit')  
        
        return redirect(f'/shows/{show_id}')  

    return redirect(f'/shows/{show_id}/edit')
# def edit_show(request, show_id):
#     show = Show().get_one(show_id)
#     if not show:
#         return redirect('/shows')
#     return render(request, "edit.html", {"show": show})


def update_show(request, show_id):
    
    if request.method == "POST":
        show = Show().get_one(show_id)
        if not show:
            return redirect('/shows')
        show.update(request.POST)
    return redirect(f"/shows/{show_id}")


def delete_show(request, show_id):
    if request.method == "POST":
        show = Show().get_one(show_id)
        if show:
            show.remove()
    return redirect("/shows")