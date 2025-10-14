from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

def index(request):
        courses = get_all(request)
        return render(request, "index.html", {'courses': courses})
    
    



def add_course(request):

    
       if request.method == "POST":
        errors = Courses.objects.validator(request)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('index')
        else:
            new_course = add_new_course(request,request.POST)
            return redirect('index')
        return redirect('/')
        
    
    
            
        


def confirm_delete_course(request, course_id):
    
    course = Courses.objects.get(id=course_id)
    course.delete()
    return redirect('/')

def destroy(request,course_id):
    context={
        'course':Courses.objects.get(id=course_id)
    }
    return render(request,'confirm_delete.html',context)

# Create your views here.
