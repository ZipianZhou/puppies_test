from django.db import models

# Create your models here.

class Post (models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    owner = models.ForeignKey('auth.User',related_name='userid',on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/loggedin/post/'+ str(self.id)

class Like(models.Model):

    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'user',)

    

