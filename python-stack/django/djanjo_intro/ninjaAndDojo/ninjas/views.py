from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .models import Dojo, Ninja


def index(request):
    dojos = Dojo.objects.all()
    ninjas = Ninja.objects.all()
    context = {
        'dojos': dojos,
        'ninjas': ninjas
    }
    return render(request, 'index.html', context)



def add_dojo(request):
    if request.method == "POST":
        
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state']
        
        if not name or not city or not state :
            messages.error(request,"Try again all dojo are required")
        else:
            Dojo.objects.create(name=name,city=city,state=state)
        
    return redirect('/')



def add_ninja(request):
    
    if request.method == "POST":
        dojo_id = request.POST['dojo_id']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dojo = Dojo.objects.filter(id=dojo_id).first()
        
        
        
        if first_name and last_name and dojo_id :
            Ninja.objects.create(first_name=first_name,last_name=last_name,dojo=dojo)
        else:
            messages.error(request,"all ninja feiled are required")
        
    
    return redirect('/')
