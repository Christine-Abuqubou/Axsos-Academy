from django.db import models
import re
import bcrypt
from django.contrib import messages
from requests import request

class User_manager(models.Manager):
    def validate(self, data):
        errors = {}
        if len(data.get('first_name','')) < 2 or not data['first_name'].isalpha():
            errors['first_name'] = "First name must be 2+ letters"
        if len(data.get('last_name','')) < 2 or not data['last_name'].isalpha():
            errors['last_name'] = "Last name must be 2+ letters"
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, data.get('email','')):
            errors['email'] = "Invalid email"
        elif User.objects.filter(email=data['email']):
            errors['email'] = "Email already exists"
            
        password = data.get('password', '')
        confirm = data.get('confirm_password', '')
        
        if len(data.get('password','')) < 8:
            errors['password'] = "Password must be 8+ chars"
        if data.get('password') != data.get('confirm_password'):
            errors['confirm'] = "Passwords do not match"
        return errors
    def login_validator(self, postData):
        errors = {}
        users = User.objects.filter(email=postData['email'])
        if len(users) == 0:
            errors['email'] = "Email not found."
        else:
            user = users[0]
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['password'] = "Incorrect password."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=User_manager()
    
    
    

def create(request,postData):
    errors=User.objects.validate(postData)
    hashed=bcrypt.hashpw(postData["password"].encode(),bcrypt.gensalt()).decode()
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
    return User.objects.create(
            first_name=postData['first_name'],
            last_name=postData['last_name'],
            email=postData['email'],
            password=hashed
        )
    