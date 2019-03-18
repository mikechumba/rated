from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import Profile,Project,Language,Rating,Contact
from .forms import Registration,LoginForm,ProfileUpdateForm,ContactUpdateForm,ProjectForm,RatingForm
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):

   title = "Rated"
   projects = Project.objects.all()

   context = {
      'projects': projects,
      'title': title
   }

   return render(request, 'rate/home.html', context)


def search(request):
   
   if 'project_search' in request.GET and request.GET["project_search"]:
      searched = request.GET.get("project_search")
      if searched:
         projects = Project.objects.filter(name=searched).all()
         title = f"You search for {searched}"

   context = {
      'projects': projects,
      'title': title,
      'searched': searched
   }

   return render(request, 'rate/search.html', context)

@login_required(login_url='register')
def profile(request):
   user = request.user

   projects = Project.objects.filter(author=user.profile)

   title = f'{user.first_name} {user.last_name}'
   context = {
      'title': title,
      'projects': projects
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
         profile = Profile(user=user)
         profile.save()

         return redirect('update_profile')
   else:
      form = Registration()

   context = {
      'title': title,
      'form': form
   }

   return render(request,'rate/register.html',context)

@login_required(login_url='register')
def edit_profile(request):

   title = f"Edit Profile | {request.user.first_name} {request.user.last_name}" 

   user = request.user

   if request.method == 'POST':
      form = ProfileUpdateForm(request.POST,request.FILES,instance=user.profile)
      contact_form = ContactUpdateForm(request.POST)
      if form.is_valid() and contact_form.is_valid():
         form.save()
         contact = contact_form.save(commit=False)
         contact.prfl = user.profile
         contact.save()
         return redirect('profile')
   else:
      form = ProfileUpdateForm(instance=user.profile)
      contact_form = ContactUpdateForm()

   context = {
      'form': form,
      'contact_form': contact_form,
      'title': title
   }

   return render(request,'rate/update_profile.html',context)

@login_required(login_url='register')
def new_project(request):

   user = request.user

   title = 'New Project'

   if request.method == 'POST':
      form = ProjectForm(request.POST,request.FILES)
      if form.is_valid():
         project = form.save(commit=False)
         project.author = user.profile
         project.save()
         return redirect('home')
   else:
      form = ProjectForm()

   context = {
      'form': form,
      'title': title
   }

   return render(request, 'rate/new_project.html',context)

@login_required(login_url='register')
def project_view(request,id):

   user = request.user

   project = Project.objects.filter(pk=id).first()

   ratings = Rating.objects.filter(rated=project)

   if ratings:
      average = ((ratings.aggregate(Sum('design'))['design__sum'])/ratings.count() + 
      ratings.aggregate(Sum('usability'))['usability__sum']/ratings.count() + 
      ratings.aggregate(Sum('content'))['content__sum']/ratings.count()) / 3
   else:
      average = '0.0'

   title = f'{project.name} by {project.author.user.first_name}'

   if request.method == 'POST':
      form = RatingForm(request.POST)
      rated = Rating.objects.filter(rated=project,rated_by=user.profile)
      if form.is_valid() and not rated:
         rating = form.save(commit=False)
         rating.rated_by = user.profile
         rating.rated = project
         rating.save()
         return redirect('project_view', id=id)
      elif form.is_valid() and rated:
         rated.delete()
         rating = form.save(commit=False)
         rating.rated_by = user.profile
         rating.rated = project
         rating.save()
         return redirect('project_view', id=id)
   else:
      form = RatingForm()

   context = {
      'title': title,
      'project': project,
      'ratings': ratings,
      'average': average,
      'form': form,
   }

   return render(request,'rate/project_view.html',context)

@login_required(login_url='register')
def logout_view(request):
   logout(request)
   return redirect('login')
