from django.db import models
from django.contrib import messages


class Course_manager(models.Manager):
    def validator(self, request):
        errors = {}
        if len(request.POST['Name']) <= 5:
            errors['Name'] = "Name should be more than 5 characters"
        if len(request.POST['Description']) <= 15:
            errors['Description'] = "Description should be more than 15 characters"
        return errors

def add_new_course(request,postData):
    errors=Courses.objects.validate(postData)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
    
        return Courses.objects.create(
            Name=postData['Name'],
            Description=postData['Description'],
        )
class Courses(models.Model):
    Name=models.CharField(max_length=100)
    Description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects= Course_manager()
    
    
    


def get_all(self):
        return Courses.objects.all()
    
    
    

# Create your models here.
