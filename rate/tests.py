from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
# Create your tests here.

def create_user_instance():
   user = User(username='johndoe',email='john@email.com',first_name='John',last_name='Doe',password='password')
   return user

def create_profile_instance(user):
   profile = Profile(user=user,avatar='default.jpg',bio="This is a bio.")
   return profile

def create_project_instance(prfl):
   project = Project(name="A Project",description="Yep! It is a project.",img="default.jpg",link="aproject.com",author=prfl)
   return project

def create_language_instance():
   language = Language(language='Python')
   return language

def create_rating_instance(project,prfl):
   review = Rating(review='A review',design=10,usability=10,content=10,rated=project,rated_by=prfl)
   return review

def create_contact_instance(prfl):
   contact = Contact(facebook="fb",twitter="twtr",instagram="insta",github="git",prfl=prfl)
   return contact

class UserTest(TestCase):

   def setUp(self):
      self.new_user = create_user_instance()

   def test_user_instance(self):
      self.assertTrue(isinstance(self.new_user,User))

   def test_save_user(self):
      self.new_user.save()
      users = User.objects.all()
      self.assertTrue(len(users),1)

class ProfileTest(TestCase):

   def setUp(self):
      self.new_user = create_user_instance()
      self.new_user.save()
      self.new_profile = create_profile_instance(self.new_user)

   def test_profile_instance(self):
      self.assertTrue(isinstance(self.new_profile,Profile))

   def test_save_profile(self):
      self.new_profile.save()
      profile = Profile.objects.all()
      self.assertTrue(len(profile),1)

class LanguageTest(TestCase):

   def setUp(self):
      self.new_language = create_language_instance()

   def test_language_instance(self):
      self.assertTrue(isinstance(self.new_language,Language))

   def test_save_language(self):
      self.new_language.save()
      languages = Language.objects.all()
      self.assertTrue(len(languages),1)

class ProjectTest(TestCase):

   def setUp(self):
      self.new_language = create_language_instance()
      self.new_language.save()
      self.new_user = create_user_instance()
      self.new_user.save()
      self.new_profile = create_profile_instance(self.new_user)
      self.new_profile.save()
      self.new_project = create_project_instance(self.new_profile)

   def test_project_instance(self):
      self.assertTrue(isinstance(self.new_project,Project))

   def test_save_project(self):
      self.new_project.save()
      self.new_project.language.add(self.new_language)
      projects = Project.objects.all()
      self.assertTrue(len(projects),1)

class ContactTest(TestCase):

   def setUp(self):
      self.new_user = create_user_instance()
      self.new_user.save()
      self.profile = create_profile_instance(self.new_user)
      self.profile.save()
      self.new_contact = create_contact_instance(self.profile)

   def test_contact_instance(self):
      self.assertTrue(isinstance(self.new_contact,Contact))

   def test_save_contact(self):
      self.new_contact.save()
      contacts = Contact.objects.all()
      self.assertTrue(len(contacts),1)

class RatingTest(TestCase):

   def setUp(self):
      self.new_user = create_user_instance()
      self.new_user.save()
      self.new_profile = create_profile_instance(self.new_user)
      self.new_profile.save()
      self.new_project = create_project_instance(self.new_profile)
      self.new_project.save()
      self.new_rating = create_rating_instance(self.new_project,self.new_profile)

   def test_rating_instance(self):
      self.assertTrue(isinstance(self.new_rating,Rating))

   def test_save_rating(self):
      self.new_rating.save()
      ratings = Rating.objects.all()
      self.assertTrue(len(ratings),1)