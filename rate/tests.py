from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
# Create your tests here.

def create_user_instance():
   user = User(username='johndoe',email='john@email.com',first_name='John',last_name='Doe',password='password')
   return user

def create_profile_instance():
   profile = Profile(user_id=1,avatar='default.jpg',bio="This is a bio.")
   return profile

def create_project_instance():
   project = Project(name="A Project",description="Yep! It is a project.",img="default.jpg",link="aproject.com")
   return project

def create_language_instance():
   language = Language(language='Python')
   return language

def create_rating_instance():
   review = Rating(review='A review',design=10,usability=10,content=10,rated_id=1,rated_by_id=1)
   return review

def create_contact_instance():
   contact = Contact(facebook="fb",twitter="twtr",instagram="insta",github="git",prfl_id=1)
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
      self.new_profile = create_profile_instance()

   def test_profile_instance(self):
      self.assertTrue(isinstance(self.new_profile,Profile))

   def test_save_profile(self):
      self.new_profile.save()
      self.new_user.save()
      profile = Profile.objects.all()
      self.assertTrue(len(profile),1)

class LanguageTest(TestCase):

   def setUp(self):
      self.new_language = create_language_instance()

   def test_language_instance(self):
      self.assertTrue(isinstance(self.new_language,Language))

class ProjectTest(TestCase):

   def setUp(self):
      self.new_project = create_project_instance()

   def test_project_instance(self):
      self.assertTrue(isinstance(self.new_project,Project))

class ContactTest(TestCase):

   def setUp(self):
      self.profile = create_profile_instance()
      self.user = create_user_instance()
      self.new_contact = create_contact_instance()

   def test_contact_instance(self):
      self.assertTrue(isinstance(self.new_contact,Contact))

   def test_save_contact(self):
      self.new_contact.save()
      # self.profile.save()
      # self.user.save()
      contacts = Contact.objects.all()
      self.assertTrue(len(contacts),1)

class RatingTest(TestCase):

   def setUp(self):
      self.new_rating = create_rating_instance()

   def test_rating_instance(self):
      self.assertTrue(isinstance(self.new_rating,Rating))
