from django.shortcuts import render ,redirect
from django.views.decorators.csrf import csrf_exempt

def index(request):
    if'counter' not in request.session :
        request.session["counter"] =0
    if "visits" not in request.session:
        request.session["visits"] =0
        
    request.session["counter"] +=1
    return  render(request,"index.html" ,{"counter" :request.session["counter"],"visits" :request.session["visits"]})

def destroy(request):
    request.session.flush()
    return redirect("index")

def increment_2(request):
    if "counter" not in request.session:
        request.session["counter"] =0
    request.session["counter"] +=2
    return redirect("index")

def increment_costum(request):
    if "counter" not in request.session:
        request.session["counter"] =0
    if request.method =="POST":
        amount=int(request.POST.get("amount", 1))
        request.session["counter"] +=amount
    return redirect("index")


    

# Create your views here.
