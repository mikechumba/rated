from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
   '''
   Holds user's profile data.
   '''

   user = models.OneToOneField(User, on_delete=models.CASCADE)
   avatar = models.ImageField(upload_to='avatars/',null=True,default='default.jpg')
   bio = models.TextField(max_length=140,null=True)

   def __str__(self):
      return self.user.username

class Language(models.Model):
   '''
   Holds data for the programming languages used.
   '''

   language = models.CharField(max_length=50)

   def __str__(self):
      return self.language

class Project(models.Model):
   '''
   Model to hold user's project data.
   '''

   author = models.ForeignKey(Profile, on_delete=models.CASCADE)
   name = models.CharField(max_length=70)
   description = models.TextField(max_length=140)
   img = models.ImageField(upload_to='projects/')
   time_published = models.DateField(auto_now=True)
   link = models.CharField(max_length=140)
   language = models.ManyToManyField(Language)
   
   def __str__(self):
      return self.name
      
class Rating(models.Model):
   '''
   Model to hold projects' ratings
   '''

   design = models.IntegerField(default=0)
   usability = models.IntegerField(default=0)
   content = models.IntegerField(default=0)
   rated = models.ForeignKey(Project, on_delete=models.CASCADE)

   def __str__(self):
      return self.rated.name

class Contact(models.Model):
   '''
   Contact class to hold the different contact details of a user
   '''

   facebook = models.CharField(max_length=70,null=True,default='#')
   twitter = models.CharField(max_length=70,null=True,default='#')
   instagram = models.CharField(max_length=70,null=True,default='#')
   github = models.CharField(max_length=70,null=True,default='#')
   prfl = models.OneToOneField(Profile, on_delete=models.CASCADE)

   def __str__(self):
      return self.prfl.user.username
