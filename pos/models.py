from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
class video(models.Model):
    video_name=models.CharField(max_length=20)
    description=models.TextField()
    file=models.FileField(upload_to='media/')
    thumbnail=models.FileField(upload_to='static/',blank=True,null=True)
    uploaded_at=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self):
        return self.video_name
class watch_historys(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    video_name=models.ForeignKey(video,on_delete=models.CASCADE)
    History=models.DateTimeField(auto_now_add=True)