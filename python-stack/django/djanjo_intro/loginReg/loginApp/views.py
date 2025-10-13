from django.shortcuts import render ,redirect
from .models import  *

def index(request):
    return render (request,"index.html")

def register(request):
    if request.method == "POST":
       
        new_user = create(request, request.POST)


        if not new_user:
            return redirect('/')

        
        request.session['user_id'] = new_user.id
        request.session['user_name'] = new_user.first_name
        return redirect('/success')

    return redirect('/')
    # create(request,request.POST)
    # return redirect('/')

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user = User.objects.get(email=request.POST['email'])
            request.session['user_id'] = user.id
            request.session['user_name'] = user.first_name
            return redirect('/success')
    
    
    return redirect("/")
 
def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, "success.html", {"name": request.session['user_name']})

def logout(request):
    request.session.flush()
    return redirect('/')   





# Create your views here.
