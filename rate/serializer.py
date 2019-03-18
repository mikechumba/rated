from rest_framework import serializers
from .models import Profile,Contact,Project
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = User
      fields = ['first_name','last_name','username','email','profile']

class  ProjectSerializer(serializers.ModelSerializer):

   class Meta:
      model = Project
      fields = ['name','author.user.first_name','author.user.last_name','description','language','link']