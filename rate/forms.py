from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Profile,Project,Contact,Rating,Language

class Registration(UserCreationForm):
   '''
   User registration form.
   '''
   first_name = forms.CharField(widget=form.TextInput(attrs={'placeholder': 'First Name'}))
   last_name = forms.CharField(widget=form.TextInput(attrs={'placeholder': 'Last Name'}))
   username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
   email= forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), max_length=64)
   password1= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
   password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))


   class Meta(UserCreationForm.Meta):
      model = User
      fields = UserCreationForm.Meta.fields + ("first_name","last_name","email","username","password1")


class LoginForm(AuthenticationForm):
   '''
   User login form.
   '''
   
   username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
   password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

   class Meta:
      model = User
      fields = ['username','password']

class ProfileUpdateForm(forms.ModelForm):
   '''
   User profile update form.
   '''

   class Meta:
      model = Profile
      fields = ['avatar', 'bio']
      widgets = {
         'bio': forms.TextInput(attrs={'placeholder': 'Enter new bio'})
      }

class ContactUpdateForm(forms.ModelForm):
   '''
   User contact update form.
   '''

   class Meta:
      model = Contact
      fields = ['facebook','twitter','instagram','github']
