from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import Profile,Project,Language,Rating,Contact
from .forms import Registration,LoginForm,ProfileUpdateForm,ContactUpdateForm

# Create your views here.
def home(request):

   title = "Rated"
   projects = Project.objects.all()

   context = {
      'projects': projects,
      'title': title
   }

   return render(request, 'rate/home.html', context)

def profile(request):
   user = request.user

   title = f'{user.first_name} {user.last_name}'
   context = {
      'title': title
   }

   return render(request,'rate/profile.html',context)


def register(request):

   title = 'Sign Up'

   if request.method == 'POST':
      form = Registration(request.POST)
      if form.is_valid():
         form.save()
         username = form.cleaned_data.get('username')
         raw_password = form.cleaned_data.get('password1')
         user = authenticate(username=username,password=raw_password)
         login(request,user)
         return redirect('home')
   else:
      form = Registration()

   context = {
      'title': title,
      'form': form
   }

   return render(request,'rate/register.html',context)