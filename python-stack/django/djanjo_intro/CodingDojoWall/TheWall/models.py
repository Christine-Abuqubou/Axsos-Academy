from django.db import models
import re
import bcrypt
from django.contrib import messages
from requests import request
from loginApp.models import User

class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    
def post_comment(self, comment, user, message):
        return self.create(comment=comment, user=user, message=message)
    
def post_message(self, message, user):
        return self.create(message=message, user=user)
    
def get_all_messages(self):
        return self.all().order_by('-created_at')



def show_all_comments(self):
        return Comment.objects.all().order_by('-created_at')
    
def delete_message(self, message_id):
        message = self.get(id=message_id)
        message.delete()
        return message
    


# Create your models here.