from django.db import models
from django.contrib.auth.models import User
from sqlalchemy import true
from django.urls import reverse
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default = User)
    thumbnail = models.ImageField(upload_to='images/')
    likeCount = models.ManyToManyField(User,related_name='blog')
    commentCount = models.IntegerField(default=0)
    description = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)

    def total_likes(self):
        return self.likeCount.count()

    def __str__(self):
        return self.title + ' | '  + str(self.author)


    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.id} )
        
    