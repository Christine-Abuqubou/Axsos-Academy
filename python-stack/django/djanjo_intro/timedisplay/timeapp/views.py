from django.shortcuts import render,HttpResponse
from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %I:%M %p", gmtime())  # Using 12-hour format
    }
    return render(request, 'time.html', context)
# Create your views here.
