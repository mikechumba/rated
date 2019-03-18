from rest_framework import serializers
from .models import Profile,Contact,Project,Language
from django.contrib.auth.models import User



class ProfileSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = Profile
      fields = ['bio']
class UserSerializer(serializers.ModelSerializer):
   profile = ProfileSerializer('profile')
   class Meta:
      model = User
      fields = ['first_name','last_name','username','email','profile']
class LanguageSerializer(serializers.ModelSerializer):
   class Meta:
      model = Language
      fields = ['language']
class PrflSerializer(serializers.ModelSerializer):
   user = UserSerializer('user')
   class Meta:
      model = Profile
      fields = ['bio','user']
class  ProjectSerializer(serializers.ModelSerializer):
   author = PrflSerializer('profile')
   language = LanguageSerializer('language',many=True)
   class Meta:
      model = Project
      fields = ['name','description','language','link','author']