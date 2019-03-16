from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
   '''
   Holds user's profile data.
   '''

   user = models.OneToOneField(User, on_delete=models.CASCADE)
   avatar = models.ImageField(upload_to='avatars/')
   bio = models.TextField(max_length=140)

   def __str__(self):
      return self.user.username

class Language(models.Model):
   '''
   Holds data for the programming languages used.
   '''

   language = models.CharField(max_length=50)
   framework = models.CharField(max_length=50)

class Rating(models.Model):
   '''
   Hold projects' ratings
   '''

   design = models.IntegerField(default=0)
   usability = models.IntegerField(default=0)
   content = models.IntegerField(default=0)

class Project(models.Model):
   '''
   To hold user's project data.
   '''

   author = models.ForeignKey(Profile, on_delete=models.CASCADE)
   name = models.CharField(max_length=70)
   description = models.TextField(max_length=140)
   img = models.ImageField(upload_to='projects/')
   time_published = models.DateField(auto_now=True)
