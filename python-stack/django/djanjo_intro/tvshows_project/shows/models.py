from django.db import models
class ShowManager(models.Manager): 
    def validate_show(self, data):
        errors = {}
        if not data.get('title') or data['title'].strip() == '':
            errors['title'] = "Title is required."
        if not data.get('network') or data['network'].strip() == '':
            errors['network'] = "Network is required."
        if not data.get('release_date') or data['release_date'].strip() == '':
            errors['release_date'] = "Release date is required."
        if not data.get('description') or len(data['description'].strip()) < 10:
            errors['description'] = "Description must be at least 10 characters."
        return errors
    def create(self, data):
        errors = self.validate_show(data)
        if errors:
            return None, errors  

        
        show = self.create(
            title=data['title'],
            network=data['network'],
            release_date=data['release_date'],
            description=data.get('description', '')
        )
        return show, None
        
        # return Show.objects.create(
        #     title=data['title'],
        #     network=data['network'],
        #     release_date=data['release_date'],
        #     description=data.get('description', '')
        # )
    def update_show(self, show, data):
        errors = self.validate_show(data)
        if errors:
            return None, errors
        show.title = data['title']
        show.network = data['network']
        show.release_date = data['release_date']
        show.description = data.get('description', '')
        show.save()
        return show, None


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()



    
    def get_one(self, show_id):
        return Show.objects.filter(id=show_id).first()  # None if not found

   
    def get_all(self):
        return Show.objects.all()

   
    # def update(self, data):
    #     self.title = data['title']
    #     self.network = data['network']
    #     self.release_date = data['release_date']
    #     self.description = data.get('description', '')
    #     self.save()
    #     return self

   
    def remove(self):
        self.delete()
        return True
    
    
    
    
