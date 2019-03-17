from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile,Project,Language,Rating,Contact
from .forms import Registration,LoginForm,ProfileUpdateForm,ContactUpdateForm

# Create your views here.
def home(request):

   projects = Project.objects.all()

   context = {
      'projects': projects
   }

   return render(request, 'rate/home.html', context)

def profile(request):

   return render(request,'rate/profile.html')
