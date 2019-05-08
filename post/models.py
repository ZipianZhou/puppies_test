from django.db import models

# Create your models here.

class Post (models.Model):
    title = models.TextField()
    cover = models.TextField()
    owner = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/loggedin/post/'+ str(self.id)
