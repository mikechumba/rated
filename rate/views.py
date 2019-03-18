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


def edit_profile(request):

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
      'contact_form': contact_form
   }

   return render(request,'rate/update_profile.html',context)

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

def project_view(request,id):

   user = request.user

   project = Project.objects.filter(pk=id).first()


   rating = Rating.objects.filter(rated=project)
   if rating:
      average = (rating.aggregate(Sum('design'))['design__sum'] + rating.aggregate(Sum('usability'))['usability__sum'] + rating.aggregate(Sum('content'))['content__sum']) / rating.count()
   else:
      average = '0.0'

   title = f'{project.name} by {project.author.user.first_name}'

   if request.method == 'POST':
      form = RatingForm(request.POST)
   else:
      form = RatingForm()

   context = {
      'title': title,
      'project': project,
      'rating': rating,
      'average': average,
      'form': form
   }

   return render(request,'rate/project_view.html',context)

def rate(request):

   user = request.user
   rating = Rating.objects.filter(rated_id=request.POST['being_rated'],rated_by=user.profile).first()
   
   if rating:

      rating.design = request.POST['dsgn']
      rating.usability = request.POST['usblty']
      rating.content = request.POST['cntnt']

      rating.save()
   else:

      rated = Rating(design=request.POST['dsgn'],usability=request.POST['usblty'],content=request.POST['cntnt'],rated_id=request.POST['being_rated'],rated_by=user.profile)
      rated.save()

   return JsonResponse(rated,safe=False)


