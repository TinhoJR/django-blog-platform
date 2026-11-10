from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    body = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="post")
    image = models.FileField(null=True,blank=True,upload_to="posts/")
    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    liked_by = models.ManyToManyField(User,related_name="posts_liked")
    # slug = models.SlugField(unique=True)


    def __str__(self):
        return self.title


    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comment")
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comment")
    comment = models.TextField()
    image = models.FileField(null=True,blank=True,upload_to="comments/")
    is_deleted = models.BooleanField(default=False)
    liked_by = models.ManyToManyField(User,related_name="comment_liked")
    last_modified = models.DateTimeField(auto_now=True)
    date = models.DateTimeField(auto_now_add=True)
    

    def delete(self, *args, **kwargs):
            self.is_deleted = True
            self.save()
            

    def __str__(self):
        return f"{self.user.username} - {self.comment}"




    
    


       
