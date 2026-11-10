from django.db import models
from django.templatetags.static import static


# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):


    def __str__(self):
        return self.username
    

class Profile(models.Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile") 
    bio = models.TextField(null=True,blank=True)
    display_photo = models.ImageField(null=True,blank=True,upload_to="profiles/")
    

    @property
    def dp(self):
        try:
            return self.display_photo.url or static("IMAGES/default_dp.jpg")
        except:
            return static("IMAGES/default_dp.jpg")


    def __str__(self):
        return self.user.username
