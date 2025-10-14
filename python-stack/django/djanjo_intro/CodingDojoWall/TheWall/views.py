from django.shortcuts import render, redirect
from django.contrib import messages
from loginApp.models import User
from .models import Message, Comment



def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    user = User.objects.get(id=request.session['user_id'])
    all_messages = Message.objects.all().order_by('-created_at')
    return render(request, "wall.html", {"user": user, "messages": all_messages})


def post_message(request):
    if request.method == "POST":
        user = User.objects.get(id=request.session['user_id'])
        Message.objects.create(user=user, content=request.POST['content'])
    return redirect('/wall')


def post_comment(request, message_id):
    if request.method == "POST":
        user = User.objects.get(id=request.session['user_id'])
        message = Message.objects.get(id=message_id)
        Comment.objects.create(
            user=user,
            message=message,
            content=request.POST['content']
        )
    return redirect('/wall')


def delete_message(request, message_id):
    user = User.objects.get(id=request.session['user_id'])
    message = Message.objects.get(id=message_id)
    # Only delete if it's the user's own message
    if message.user == user:
        message.delete()
    return redirect('/wall')
