from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile,Project,Language,Rating,Contact

# Create your views here.
def home(request):


   context = {

   }

   return render(request, 'rate/home.html', context)