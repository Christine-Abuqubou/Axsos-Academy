from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

 
    def create(self, data):
        return Show.objects.create(
            title=data['title'],
            network=data['network'],
            release_date=data['release_date'],
            description=data.get('description', '')
        )

    
    def get_one(self, show_id):
        return Show.objects.filter(id=show_id).first()  # None if not found

   
    def get_all(self):
        return Show.objects.all()

   
    def update(self, data):
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data.get('description', '')
        self.save()
        return self

   
    def remove(self):
        self.delete()
        return True
